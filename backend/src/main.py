from fastapi import FastAPI

from src.routers import item, user

app = FastAPI()

app.include_router(item.router, prefix="/api/v1/item")
app.include_router(user.router, prefix="/api/v1/user")
