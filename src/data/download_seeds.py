"""Download the UCI Seeds dataset."""
import requests
import zipfile
import io
from pathlib import Path

URL = "https://archive.ics.uci.edu/static/public/236/seeds.zip"
RAW_DIR = Path(__file__).resolve().parent / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)


def download() -> None:
    response = requests.get(URL, timeout=30)
    response.raise_for_status()

    with zipfile.ZipFile(io.BytesIO(response.content)) as zf:
        zf.extractall(RAW_DIR)

    print(f"Dataset extraído em: {RAW_DIR}")
    print("Arquivos:", [p.name for p in RAW_DIR.iterdir()])


if __name__ == "__main__":
    download()
