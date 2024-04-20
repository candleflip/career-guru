import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/health-check")
def health_check():
    return {"ping": "pong"}


if __name__ == "__main__":
    uvicorn.run(app=app)
