from fastapi import FastAPI
from wealth_estimator.api import predictions

app = FastAPI()

app.include_router(predictions.router, tags=["predictions"])
