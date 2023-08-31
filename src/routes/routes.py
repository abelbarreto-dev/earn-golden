from fastapi import APIRouter

from fastapi import Response


def get_route() -> APIRouter:
    return APIRouter()


route = get_route()


@route.get("/")
async def root() -> Response:
    return Response(
        content={
            "message": "Hello World! I'm EarnGolden."
        }
    )
