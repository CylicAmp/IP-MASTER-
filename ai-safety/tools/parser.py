"""
parser.py
Ingests LLM transcripts in JSON or Markdown format and returns
a structured list of messages with speaker labels.
"""

import json
import re
from pathlib import Path


def parse_markdown(filepath: str) -> list[dict]:
    """
    Parse a Markdown transcript where messages are separated by
    speaker headers like '**User:**' or '**Assistant:**'
    Returns list of dicts: [{"speaker": str, "text": str}, ...]
    """
    text = Path(filepath).read_text(encoding="utf-8")
    messages = []
    pattern = re.compile(
        r"\*\*(User|Assistant|Human|LLM|AI):\*\*\s*(.*?)(?=\*\*(User|Assistant|Human|LLM|AI):\*\*|\Z)",
        re.DOTALL | re.IGNORECASE
    )
    for match in pattern.finditer(text):
        speaker = match.group(1).strip()
        content = match.group(2).strip()
        if content:
            messages.append({"speaker": speaker, "text": content})
    return messages


def parse_json(filepath: str) -> list[dict]:
    """
    Parse a JSON transcript. Expects format:
    [{"role": "user" | "assistant", "content": "..."}, ...]
    """
    data = json.loads(Path(filepath).read_text(encoding="utf-8"))
    messages = []
    for entry in data:
        role = entry.get("role", entry.get("speaker", "unknown"))
        content = entry.get("content", entry.get("text", ""))
        if content:
            messages.append({"speaker": role, "text": content})
    return messages


def parse_raw_text(filepath: str) -> list[dict]:
    """
    Parse a plain text transcript. Lines starting with 'User:' or
    'Assistant:' are treated as speaker turns.
    """
    text = Path(filepath).read_text(encoding="utf-8")
    messages = []
    current_speaker = None
    current_lines = []

    for line in text.splitlines():
        match = re.match(r"^(User|Assistant|Human|LLM|AI):\s*(.*)", line, re.IGNORECASE)
        if match:
            if current_speaker and current_lines:
                messages.append({
                    "speaker": current_speaker,
                    "text": " ".join(current_lines).strip()
                })
            current_speaker = match.group(1)
            current_lines = [match.group(2)]
        elif current_speaker:
            current_lines.append(line)

    if current_speaker and current_lines:
        messages.append({
            "speaker": current_speaker,
            "text": " ".join(current_lines).strip()
        })

    return messages


def load_transcript(filepath: str) -> list[dict]:
    """
    Auto-detect format and parse transcript.
    Supports .json, .md, .txt
    """
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"Transcript not found: {filepath}")

    suffix = path.suffix.lower()
    if suffix == ".json":
        return parse_json(filepath)
    elif suffix in (".md", ".markdown"):
        return parse_markdown(filepath)
    else:
        return parse_raw_text(filepath)
