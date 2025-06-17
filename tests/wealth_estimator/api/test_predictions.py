import json
from pathlib import Path
from unittest.mock import patch
import numpy as np
from fastapi.testclient import TestClient
from wealth_estimator.api.main import app
from wealth_estimator.core.logger import Logger

client = TestClient(app)

def test_predict_selfie_happy_path():
    extract_face_embedding_return_value = {}
    with open(Path('tests/test_data/warren_buffett.json'), "r") as f:
        extract_face_embedding_return_value = [np.array(json.loads(f.read())['warren_buffett']['embedding'])]
    with open(Path('tests/test_data/warren_buffett.jpg'), "rb") as f, \
        patch('wealth_estimator.services.utils.face_recognition.face_encodings', return_value=extract_face_embedding_return_value), \
        patch(
            'wealth_estimator.services.logic.cosine_similarity', 
            return_value=[np.array(
                [0.86786353,0.79310643,0.80702359,0.84250704,0.80878076,0.72954176,0.93514087]
            )]
        ): 
        response = client.post(
            "/predict",
            files={"image": ("warren_buffett.jpg", f, "image/jpeg")},
            data={"top_n_similar": 3}
        )
        assert response.status_code == 200
        assert response.json() == {
            "estimated_net_worth": 164210828075, # Weighted average of the net worths of the 3 matches below, weighted by similarity 
            "top_matches": [
                {"name": "warren_buffett", "similarity": 0.9351}, 
                {"name": "bill_gates", "similarity": 0.8679}, 
                {"name": "jeff_bezos", "similarity": 0.8425}
            ]
        }

def test_predict_selfie_invalid_content_type():
    response = client.post(
        "/predict",
        files={"image": ("fake.txt", b"not-an-image", "text/plain")},
        data={"top_n_similar": 3}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid file type"

def test_predict_selfie_invalid_top_n_similar():
    response = client.post(
        "/predict?top_n_similar=0",
        files={"image": ("face.jpg", b"fake-image-bytes", "image/jpeg")}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "top_n_similar must be greater than 0"

def test_value_error_from_get_matches():
    with open(Path('tests/test_data/warren_buffett.jpg'), "rb") as f, \
    patch("wealth_estimator.api.predictions.extract_face_embedding", side_effect=ValueError("Internal error")):
        response = client.post(
            "/predict",
            files={"image": ("face.jpg", f, "image/jpeg")},
            data={"top_n_similar": 3}
        )
        assert response.status_code == 503
        assert response.json()["detail"] == "Internal error"