from pydantic import BaseModel
from typing import List

class Match(BaseModel):
    name: str
    similarity: float

class PredictionResponse(BaseModel):
    estimated_net_worth: float
    top_matches: List[Match]
