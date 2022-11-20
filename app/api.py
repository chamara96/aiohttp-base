from aiohttp import web
from app.models.models import *
from app import db


async def healthcheck(request: web.Request):
    """
    Health check endpoint
    """
    return web.json_response({"status": "OK"}, status=200)
