import asyncio
import json
from pathlib import Path

import click
from fastapi.testclient import TestClient
from wealth_estimator.api.main import app

IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'}

client = TestClient(app)

@click.command()
@click.option("--image_path", help="Path containing image to determine top similar faces and wealth")
@click.option("--top_n_similar", default=3, help="How many top similar images to return")
def run_locally(image_path, top_n_similar) -> dict:
    """
    Run the program locally for local development to get the top N most similar people, 
    and the estimated net worth for the given picture.

    :image_path: Path containing image to get matches and estimate wealth for.
    :top_n_similar: How many of the top similar people to return.
    :return: Dict of data containing {
        "estimated_net_worth" (int): Weighted average of net worth between the top N matches, weighted by similarity
        "matches": {
            "name": name of match,
            "similarity" (float): similarity score of match
        } 
    }.
    """
    with open(image_path, "rb") as img_file:
        response = client.post(
            "/predict",
            files={"image": (Path(image_path).name, img_file, "image/jpeg")},
            data={"top_n_similar": top_n_similar},
        )
        print("Status code:", response.status_code)
    try:
        response.raise_for_status()
        print(json.dumps(response.json(), indent=2))
    except Exception as e:
        print("Error response:", response.text)
    return response.json()

if __name__ == "__main__":
    run_locally()