import os

import asyncpg
import redis.asyncio as redis
from fastapi import FastAPI

app = FastAPI()

DATABASE_URL = os.environ["DATABASE_URL"]
REDIS_URL = os.environ["REDIS_URL"]


@app.get("/")
async def root() -> dict[str, str]:
    return {"service": "api", "status": "running"}


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/ready")
async def ready() -> dict[str, str]:
    postgres = await asyncpg.connect(DATABASE_URL)
    try:
        await postgres.execute("SELECT 1")
    finally:
        await postgres.close()

    redis_client = redis.from_url(REDIS_URL)
    try:
        await redis_client.ping()
    finally:
        await redis_client.aclose()

    return {
        "status": "ready",
        "postgres": "ok",
        "redis": "ok",
    }
