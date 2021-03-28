import pymongo
from starlette.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware


class DatabaseMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
      client = pymongo.MongoClient()
      db = client["food"]
      request.state.db = db
      response = await call_next(request)
      return response


middleware = [
    Middleware(DatabaseMiddleware)
]
