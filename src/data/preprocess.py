"""Preprocess the UCI Seeds dataset."""
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

RAW_DIR = Path(__file__).resolve().parent / "raw"
PROCESSED_DIR = Path(__file__).resolve().parent / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

COLUMNS = [
    "area",
    "perimeter",
    "compactness",
    "kernel_length",
    "kernel_width",
    "asymmetry_coefficient",
    "groove_length",
    "variety",
]
VARIETY_MAP = {1: "Kama", 2: "Rosa", 3: "Canadian"}


def load_raw() -> pd.DataFrame:
    paths = list(RAW_DIR.rglob("*"))
    candidates = [p for p in paths if p.is_file() and "seeds" in p.name.lower()]
    if not candidates:
        raise FileNotFoundError(f"Arquivo seeds não encontrado em {RAW_DIR}. Execute download_seeds.py primeiro.")

    data_path = candidates[0]
    df = pd.read_csv(data_path, sep=r"\s+", header=None, names=COLUMNS)
    df["variety"] = df["variety"].map(VARIETY_MAP)
    return df


def preprocess() -> None:
    df = load_raw()

    features = [c for c in COLUMNS if c != "variety"]
    X = df[features]
    y = df["variety"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.30, random_state=42, stratify=y
    )

    scaler = StandardScaler()
    X_train_scaled = pd.DataFrame(scaler.fit_transform(X_train), columns=features, index=X_train.index)
    X_test_scaled = pd.DataFrame(scaler.transform(X_test), columns=features, index=X_test.index)

    train_df = X_train_scaled.copy()
    train_df["variety"] = y_train.values
    test_df = X_test_scaled.copy()
    test_df["variety"] = y_test.values

    df.to_csv(PROCESSED_DIR / "seeds_full.csv", index=False)
    train_df.to_csv(PROCESSED_DIR / "seeds_train.csv", index=False)
    test_df.to_csv(PROCESSED_DIR / "seeds_test.csv", index=False)

    print(f"Dados processados salvos em {PROCESSED_DIR}")
    print(f"Treino: {len(train_df)} amostras | Teste: {len(test_df)} amostras")


if __name__ == "__main__":
    preprocess()
