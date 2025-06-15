import json
from pathlib import Path

import click
from wealth_estimator.app.main import get_matches

IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'}

@click.command()
@click.option("--image_path", help="Path containing image to determine top similar faces and wealth")
@click.option("--top_n_similar", default=3, help="How many top similar images to return")
def run_get_matches(image_path, top_n_similar):
    with open(Path(image_path), "rb") as f:
        results = get_matches(f, top_n_similar)
    print(json.dumps(results))
    return results

if __name__ == "__main__":
    print(run_get_matches())