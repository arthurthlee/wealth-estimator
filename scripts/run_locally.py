import asyncio
import json
from pathlib import Path

import click
from wealth_estimator.app.main import get_matches_and_estimated_net_worth

IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'}

@click.command()
@click.option("--image_path", help="Path containing image to determine top similar faces and wealth")
@click.option("--top_n_similar", default=3, help="How many top similar images to return")
def run_locally(image_path, top_n_similar) -> dict:
    """
    Run the get_matches_and_estimated_net_worth function locally for local development to get the top N most similar people, 
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
    async def run():
        with open(Path(image_path), "rb") as f:
            results = await get_matches_and_estimated_net_worth(f, top_n_similar)
        print(json.dumps(results))
        return results
    asyncio.run(run())

if __name__ == "__main__":
    print(run_locally())