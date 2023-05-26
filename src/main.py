from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from src.auth.base_config import auth_backend, fastapi_users
from src.auth.schemas import UserRead, UserCreate
from src.operations.router import router as operation_router
from src.tasks.router import router as tasks_router
from src.pages.router import router as pages_router
from src.chat.router import router as chat_router

app = FastAPI(title='Trading App')

app.mount('/static', StaticFiles(directory='src/static'), name='static')

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(operation_router)
app.include_router(tasks_router)
app.include_router(pages_router)
app.include_router(chat_router)

origins = [
    'http://localhost',
    'http://127.0.0.1',
    'http://localhost:3000',
    'http://127.0.0.1:3000',
    'http://localhost:8000',
    'http://127.0.0.1:8000',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'OPTIONS', 'DELETE', 'PUT', 'PATCH', 'HEAD'],
    allow_headers=['Content-Type', 'Set-Cookie', 'Access-Control-Allow-Headers', 'Access-Control-Allow-Origins',
                   'Authorization'],
)


@app.on_event('startup')
async def startup_event():
    redis = aioredis.from_url('redis://localhost', encoding='utf8', decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix='fastapi-cache')
