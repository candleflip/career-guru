from fastapi import FastAPI

from app.api import health_check

app = FastAPI()
app.include_router(router=health_check.router, tags=["health-check"])
