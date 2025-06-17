from wealth_estimator.services.utils import extract_face_embedding
import numpy as np
import json
from numpy.testing import assert_array_equal

def test_extract_face_embedding_face_exists():
    with open('scripts/data/pictures/warren_buffett.jpg', "rb") as f, \
        open('wealth_estimator/data/data.json', "r") as expected_data:
        image_bytes = f.read()
        embedding = extract_face_embedding(image_bytes)
        print(expected_data)
        expected = np.array(json.loads(expected_data.read())['warren_buffett']['embedding'])
        assert_array_equal(embedding, expected)

def test_extract_face_embedding_no_face_exists():
    with open('tests/test_data/not_a_face.jpg', "rb") as f:
        image_bytes = f.read()
        embedding = extract_face_embedding(image_bytes)
        assert embedding.size == 0
