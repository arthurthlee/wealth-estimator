from fastapi import FastAPI, UploadFile, File, HTTPException
from wealth_estimator.app.utils import extract_face_embedding
from wealth_estimator.app.logic import find_top_matches
from wealth_estimator.app.models import PredictionResponse

app = FastAPI()

def get_matches(image: UploadFile = File(...), top_n_similar: int = 3):
    image_bytes = image.read()
    embedding = extract_face_embedding(image_bytes)
    matches, estimated_wealth = find_top_matches(embedding, top_n_similar)
    return {
        "estimated_net_worth": estimated_wealth,
        "top_matches": matches
    }


@app.post("/predict", response_model=PredictionResponse)
def predict_selfie(image: UploadFile = File(...), top_n_similar: int = 3):
    if top_n_similar < 1:
        raise HTTPException(status_code=400, detail="top_n_similar must be greater than 0")
    if not image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid file type")
    try:
        return get_matches(image, top_n_similar)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
