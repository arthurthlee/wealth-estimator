from fastapi import FastAPI, UploadFile, File, HTTPException
from wealth_estimator.app.utils import extract_face_embedding
from wealth_estimator.app.logic import find_top_matches
from wealth_estimator.app.models import PredictionResponse

app = FastAPI()


@app.post("/predict", response_model=PredictionResponse)
async def predict_selfie(image: UploadFile = File(...), top_n_similar: int = 3):
    """
    Get dict of top N matches and estimated net worth for a given image

    :image: File uploaded in a request.
    :top_n_similar: Top N matches to return
    :return: dict
    """
    if top_n_similar < 1:
        raise HTTPException(status_code=400, detail="top_n_similar must be greater than 0")
    if not image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid file type")
    try:
        image_bytes = await image.read()
        embedding = extract_face_embedding(image_bytes)
        matches, estimated_wealth = find_top_matches(embedding, top_n_similar)
        return {
            "estimated_net_worth": estimated_wealth,
            "top_matches": matches
        }

    except ValueError as e:
        raise HTTPException(status_code=503, detail=str(e))
