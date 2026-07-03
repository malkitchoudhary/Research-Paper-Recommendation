import pickle
import re
from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Paper Explorer",
    page_icon="📄",
    layout="wide",
)

DATA_DIR = Path(__file__).resolve().parent
PAPER_PATH = DATA_DIR / "paper.pkl"
SIM_PATH = DATA_DIR / "similarity.pkl"


@st.cache_resource
def load_papers() -> pd.DataFrame:
    with open(PAPER_PATH, "rb") as file:
        papers = pickle.load(file)
    if not isinstance(papers, pd.DataFrame):
        raise ValueError("paper.pkl must contain a pandas DataFrame")
    return papers


@st.cache_resource
def load_similarity() -> np.ndarray:
    with open(SIM_PATH, "rb") as file:
        similarity = pickle.load(file)
    if not isinstance(similarity, np.ndarray):
        raise ValueError("similarity.pkl must contain a numpy ndarray")
    return similarity


@st.cache_data
def search_papers(query: str, papers: pd.DataFrame, max_results: int = 100) -> pd.DataFrame:
    query = query.strip()
    if not query:
        return papers.head(max_results)

    query_pattern = re.escape(query)
    title_match = papers["title"].astype(str).str.contains(query_pattern, case=False, na=False)
    text_match = papers["new_paper_text"].astype(str).str.contains(query_pattern, case=False, na=False)
    found = papers[title_match | text_match]

    if found.empty:
        tokens = [re.escape(tok) for tok in query.split() if tok]
        if tokens:
            fuzzy_pattern = "|".join(tokens)
            fuzzy_match = (
                papers["title"].astype(str).str.contains(fuzzy_pattern, case=False, na=False)
                | papers["new_paper_text"].astype(str).str.contains(fuzzy_pattern, case=False, na=False)
            )
            found = papers[fuzzy_match]

    return found.head(max_results)


def get_similar_papers(index: int, similarity: np.ndarray, top_n: int = 10) -> np.ndarray:
    scores = similarity[index]
    ranking = np.argsort(scores)[::-1]
    ranking = ranking[ranking != index]
    return ranking[:top_n]


def clean_paper_text(text: str) -> str:
    """Remove concatenated filename from start of paper text (PDF extraction artifact)"""
    text = text.strip()
    if not text:
        return text
    
    # If text starts with a very long word (likely concatenated filename from PDF), remove it
    first_word = text.split()[0] if text.split() else ""
    if len(first_word) > 40 and first_word.isalpha():
        # Remove the concatenated filename and rejoin with remaining text
        text = " ".join(text.split()[1:])
    
    return text.strip()


def render_paper_card(title: str, text: str, score: float | None = None) -> None:
    score_str = f"**Similarity:** {score:.3f}" if score is not None else ""
    st.markdown(f"**{title}**  \n{score_str}")
    preview = clean_paper_text(text).replace("\n", " ")
    if len(preview) > 500:
        preview = preview[:500].rsplit(" ", 1)[0] + "..."
    st.write(preview)


def main() -> None:
    papers = load_papers()
    similarity = load_similarity()

    st.title("Paper Explorer")
    st.write(
        "Browse the paper collection, search by title or keywords, and discover related papers "
        "using the precomputed similarity matrix."
    )

    with st.sidebar:
        st.header("Search")
        query = st.text_input("Enter a title or keyword", "")
        top_n = st.slider("Number of related papers to show", min_value=3, max_value=20, value=10)
        if query:
            results = search_papers(query, papers)
        else:
            results = papers.head(50)

        st.write(f"Found **{len(results)}** matching papers")
        options = [f"{idx} | {title}" for idx, title in zip(results.index, results["title"])]
        selected_option = st.selectbox("Select a paper to explore", options)

    if selected_option:
        selected_idx = int(selected_option.split(" | ", 1)[0])
        selected_row = papers.loc[selected_idx]

        st.subheader("Selected Paper")
        render_paper_card(selected_row["title"], selected_row["new_paper_text"])

        st.subheader("Related Papers")
        similar_ids = get_similar_papers(selected_idx, similarity, top_n=top_n)
        for idx in similar_ids:
            row = papers.loc[idx]
            render_paper_card(row["title"], row["new_paper_text"], float(similarity[selected_idx, idx]))

    st.sidebar.markdown("---")
    st.sidebar.markdown(
        "This app loads `paper.pkl` and `similarity.pkl` from the same folder as `app.py`. "
        "Use the search box to find a paper, then view its top similar papers."
    )


if __name__ == "__main__":
    main()
