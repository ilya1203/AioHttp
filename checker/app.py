from aiohttp import web
from .routers import setup_router


async def create_app():
    app = web.Application()
    setup_router(app)
    return app
