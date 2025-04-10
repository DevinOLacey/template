from fastapi import FastAPI
from authenticator import authenticator
from routers.users import router as users_router
from routers.roles import router as roles_router
from fastapi.middleware.cors import CORSMiddleware
import os
import subprocess
from routers import users, roles, pages

# Run database migrations
print("Running database migrations...")
subprocess.run(["python", "db/migrate.py"], check=True)

# from routers import user  # Example router

app = FastAPI()

# Get allowed origins from environment variable or use default in development
ALLOWED_ORIGINS = os.getenv(
    "ALLOWED_ORIGINS", "http://localhost:5173,http://127.0.0.1:5173"
)

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS.split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Authentication routes
app.include_router(authenticator.router, tags=["Authentication"])

# User management routes
app.include_router(users_router, tags=["Users"])
app.include_router(users.router, tags=["Users"])

# Role management routes
app.include_router(roles_router, tags=["Roles"])
app.include_router(roles.router, tags=["Roles"])

# Access management routes
app.include_router(pages.router, tags=["Access Management"])


@app.get("/")
def root():
    return {"message": "Welcome to the backend!"}


# Only create Lambda handler if running in AWS Lambda
if os.getenv("AWS_LAMBDA_FUNCTION_NAME"):
    try:
        from mangum import Mangum

        handler = Mangum(app, lifespan="off")
    except ImportError:
        pass
