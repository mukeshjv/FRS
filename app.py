from starlette.applications import Starlette
from starlette.routing import Route
from starlette.staticfiles import StaticFiles
from routes import homepage, findrecipe
from middleware import middleware


app = Starlette(debug=True, routes=[
    Route('/', homepage),
    Route('/findrecipe', findrecipe, methods=["GET", "POST"])
] , middleware=middleware)

app.mount(
    '/static', StaticFiles(directory='/home/mukesh/Documents/FRS/static/'))
