import json
from pathlib import Path
import click
import pandas as pd
from wealth_estimator.services.utils import extract_face_embedding

IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'}

@click.command()
@click.option("--pictures_folder", default=Path("scripts/data/pictures"), help="Path containing pictures")
@click.option("--net_worths_file", default=Path("scripts/data/net_worths.csv"), help="Path containing net worths csv file")
def create_embeddings(pictures_folder: Path, net_worths_file: Path):
    """
    Creates embeddings for every picture in the given picture folder, 
    assigns the net worth to each picture with the matching person in the net_worths_file, 
    and then outputs the resulting dict into a json file.

    :pictures_folder: Path containing pictures to create embeddings for.
    :net_worths_file: Path containing net worths file to match embeddings.
    :return: Dict of data containing {
        "firstname_lastname": {
            "embedding": ndarray,
            "net_worth": int
        }
    }.
    """
    data = {}
    df = pd.read_csv(net_worths_file)
    for file in Path(pictures_folder).iterdir():
        print(file)
        # Skip over all items that are not files or images
        if file.is_file() and file.suffix.lower() in IMAGE_EXTENSIONS and file not in data:
            with open(Path(file), "rb") as f:
                data[file.stem] = {
                    "embedding": extract_face_embedding(f.read()).tolist(),
                    "net_worth": df.loc[df['name'] == file.stem, 'net_worth'].values[0].item()
                }
    folder = Path('wealth_estimator/data')
    folder.mkdir(parents=True, exist_ok=True)
    results = json.dumps(data)
    with open(folder/"data.json", "w", encoding="utf-8") as f:
        f.write(results)
    print(f"Created embeddings file at {folder/'data.json'}")
    return data

if __name__ == "__main__":
    create_embeddings()