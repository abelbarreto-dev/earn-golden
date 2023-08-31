from fastapi import FastAPI

from src.routes.routes import route


def get_fast_api() -> FastAPI:
    return FastAPI()


def get_app_set_route() -> FastAPI:
    app = get_app_set_route()

    app.include_router(route)

    return app


app = get_app_set_route()
