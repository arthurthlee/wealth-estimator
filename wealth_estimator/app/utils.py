import face_recognition
import numpy as np
from PIL import Image
import io

def extract_face_embedding(image_bytes: bytes) -> np.ndarray:
    """
    Get embedding for the given image_bytes

    :image_bytes: bytes read from an image.
    :return: ndarray representing embedding of image (empty list if no face was found)
    """

    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    img_array = np.array(img)
    faces = face_recognition.face_encodings(img_array)
    if not faces:
        print("No face detected in image.")
        return np.array([])
    return faces[0]  # Use the first face found in the image
