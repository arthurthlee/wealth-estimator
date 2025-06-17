from fastapi import FastAPI
from wealth_estimator.api import predictions

app = FastAPI()

app.include_router(predictions.router, tags=["predictions"])

@app.get("/")
def health_check():
    return {"status": "ok"}  # AWS ECS will consider 200 OK as healthy