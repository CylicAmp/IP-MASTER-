from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware


class FilterMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, filter_func):
        super().__init__(app)
        self.filter_func = filter_func

    async def dispatch(self, request: Request, call_next):
        if request.headers.get("content-type") != "text/plain":
            return await call_next(request)
        body = await request.body()
        text = body.decode("utf-8")
        filtered = self.filter_func(text)

        async def receive():
            return {"type": "http.request", "body": filtered.encode()}

        new_request = Request(request.scope, receive=receive)
        return await call_next(new_request)


# Usage
app = FastAPI()
app.add_middleware(FilterMiddleware, filter_func=lambda t: t.replace("foo", "bar"))
