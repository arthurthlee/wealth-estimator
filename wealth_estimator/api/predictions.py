from fastapi import APIRouter, UploadFile, File, HTTPException
from wealth_estimator.core.logger import Logger
from wealth_estimator.services.utils import extract_face_embedding
from wealth_estimator.services.logic import find_top_matches
from wealth_estimator.models.models import PredictionResponse

router = APIRouter()
log = Logger.get_logger('predictions')

@router.post("/predict", response_model=PredictionResponse)
async def predict_selfie(image: UploadFile = File(...), top_n_similar: int = 3):
    """
    Get dict of top N matches and estimated net worth for a given image

    :image: File uploaded in a request.
    :top_n_similar: Top N matches to return
    :return: dict
    """
    if top_n_similar < 1:
        error_msg = "top_n_similar must be greater than 0"
        log.error(error_msg)
        raise HTTPException(status_code=400, detail=error_msg)
    if not image.content_type.startswith("image/"):
        error_msg = "Invalid file type"
        log.error(error_msg)
        raise HTTPException(status_code=400, detail=error_msg)
    try:
        image_bytes = await image.read()
        embedding = extract_face_embedding(image_bytes)
        matches, estimated_wealth = find_top_matches(embedding, top_n_similar)
        return {
            "estimated_net_worth": estimated_wealth,
            "top_matches": matches
        }

    except ValueError as e:
        error_msg = str(e)
        log.error(error_msg)
        raise HTTPException(status_code=503, detail=error_msg)