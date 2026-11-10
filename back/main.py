from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware.trustedhost import TrustedHostMiddleware
from contextlib import asynccontextmanager
from db import database

# 
# FastAPI Setup
# 

@asynccontextmanager
async def lifespan(app: FastAPI):
    database.migrate()
    yield

app = FastAPI(lifespan=lifespan)


# 
# Prevent write requests from unauthorised
# 

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["127.0.0.1"],
)

ALLOWED_WRITE_ORIGINS = {
    "http://127.0.0.1:5173",    # Vite during development
}

WRITE_METHODS = {"POST", "PUT", "PATCH", "DELETE"}

@app.middleware("http")
async def check_write_origin(request: Request, call_next):
    if request.method in WRITE_METHODS:
        origin = request.headers.get("origin")

        if origin not in ALLOWED_WRITE_ORIGINS:
            return JSONResponse(
                status_code=403,
                content={"detail": "Origin not allowed"},
            )

    return await call_next(request)


# 
# Router
# 

from routes import router

app.include_router(router)