from fastapi import FastAPI, UploadFile, File, HTTPException
from app.utils import extract_face_embedding
from app.logic import find_top_matches
from app.models import PredictionResponse

app = FastAPI()

@app.post("/predict", response_model=PredictionResponse)
async def predict_selfie(image: UploadFile = File(...), top_n_similar: int = 3):
    if not image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid file type")

    try:
        image_bytes = image.read()
        embedding = extract_face_embedding(image_bytes)
        matches, estimated_wealth = find_top_matches(embedding, top_n_similar)

        return {
            "estimated_net_worth": estimated_wealth,
            "top_matches": matches
        }

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
