"""
Utility script to (re)generate similarity matrices for the Streamlit app.

Usage:
    python scripts/generate_similarity.py

Requirements:
    - movie_dict.pkl must exist in the project root.
    - pandas and scikit-learn must be installed.
"""

from __future__ import annotations

import argparse
import pickle
from pathlib import Path
from typing import Any

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


PROJECT_ROOT = Path(__file__).resolve().parent.parent
MOVIE_DICT_PATH = PROJECT_ROOT / "movie_dict.pkl"
SIMILARITY_PATH = PROJECT_ROOT / "similarity.pkl"


def _normalize_tags(value: Any) -> str:
    """Ensure every tag entry is a whitespace separated string."""
    if isinstance(value, list):
        return " ".join(str(item) for item in value)
    return str(value)


def generate_similarity(max_features: int = 5000) -> None:
    """Generate and persist the cosine similarity matrix."""
    if not MOVIE_DICT_PATH.exists():
        raise FileNotFoundError(
            "movie_dict.pkl not found. Run the notebook first to create it."
        )

    with MOVIE_DICT_PATH.open("rb") as file:
        movie_dict = pickle.load(file)

    movies_df = pd.DataFrame(movie_dict)
    if "tags" not in movies_df.columns:
        raise KeyError("The movie dictionary must contain a 'tags' column.")

    movies_df["tags"] = movies_df["tags"].apply(_normalize_tags)

    vectorizer = CountVectorizer(
        max_features=max_features,
        stop_words="english",
    )
    vectors = vectorizer.fit_transform(movies_df["tags"])
    similarity = cosine_similarity(vectors)

    with SIMILARITY_PATH.open("wb") as file:
        pickle.dump(similarity, file)

    print(f"✅ similarity.pkl created at {SIMILARITY_PATH}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate similarity.pkl for the Streamlit app."
    )
    parser.add_argument(
        "--max-features",
        type=int,
        default=5000,
        help="Maximum vocabulary size for CountVectorizer.",
    )
    args = parser.parse_args()
    generate_similarity(max_features=args.max_features)


if __name__ == "__main__":
    main()

