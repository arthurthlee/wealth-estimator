import json
from pathlib import Path
import click
import pandas as pd
from wealth_estimator.app.utils import extract_face_embedding

IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'}

@click.command()
@click.option("--pictures_folder", default=Path("data/pictures"), help="Path containing pictures")
@click.option("--net_worths_file", default=Path("data/net_worths.csv"), help="Path containing net worths csv file")
def create_embeddings(pictures_folder, net_worths_file):
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
    with open(folder/"data.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(data))
    print(f"Created embeddings file at {folder/'data.json'}")

if __name__ == "__main__":
    create_embeddings()