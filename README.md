# 📚 Research Paper Recommendation System

### An NLP-Powered Research Paper Recommendation System using Machine Learning and Streamlit

<p align="center">
  <img src="recommendation.gif" alt="Project Demo" width="100%">
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?style=for-the-badge&logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?style=for-the-badge&logo=scikitlearn)
![NLP](https://img.shields.io/badge/NLP-CountVectorizer-success?style=for-the-badge)

</p>

---

## 📌 Overview

The **Research Paper Recommendation System** is a Machine Learning and Natural Language Processing (NLP) project that helps users discover research papers related to their interests. It uses **Content-Based Filtering** to recommend papers based on textual similarity.

The application features an interactive **Streamlit** web interface where users can search for papers using titles or keywords, explore paper previews, and receive personalized recommendations in real time.

The recommendation engine is powered by **CountVectorizer** and **Cosine Similarity**, enabling fast and accurate retrieval of related research papers from the dataset.

---

## ✨ Features

### 🤖 Machine Learning

- Content-Based Recommendation System
- NLP Text Preprocessing
- CountVectorizer Feature Extraction
- Cosine Similarity Recommendation Engine
- Precomputed Similarity Matrix
- Fast Recommendation Retrieval

### 🌐 Streamlit Web Application

- Interactive User Interface
- Search by Paper Title
- Search by Keywords
- Paper Preview
- Top-N Similar Paper Recommendations
- Adjustable Number of Recommendations
- Cached Data Loading for Better Performance
- Clean and Responsive Layout

---

## 🏗️ System Architecture

```text
                 Research Papers Dataset
                          │
                          ▼
                Text Preprocessing (NLP)
                          │
                          ▼
                 CountVectorizer Model
                          │
                          ▼
                  Feature Vector Matrix
                          │
                          ▼
                 Cosine Similarity Matrix
                          │
          ┌───────────────┴───────────────┐
          ▼                               ▼
      paper.pkl                    similarity.pkl
          │                               │
          └───────────────┬───────────────┘
                          ▼
               Streamlit Recommendation App
                          │
                          ▼
      Search → Select Paper → View Recommendations
```

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| Frontend | Streamlit |
| Machine Learning | Scikit-learn |
| NLP | CountVectorizer |
| Data Processing | Pandas, NumPy |
| Similarity Metric | Cosine Similarity |
| Model Storage | Pickle |
| Development | Jupyter Notebook |

---

## 📂 Project Structure

```text
Research-Paper-Recommendation-System/
│
├── app.py
├── researchpaper.ipynb
├── paper.pkl
├── similarity.pkl
├── recommendation.gif
├── requirements.txt
├── README.md
│
├── images/
│   ├── home.png
│   └── recommendation.png
│
└── dataset/
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Research-Paper-Recommendation-System.git
```

Navigate to the project folder

```bash
cd Research-Paper-Recommendation-System
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

Open your browser and visit

```
http://localhost:8501
```

---

## 🚀 Application Workflow

1. Load the processed research paper dataset.
2. Load the precomputed similarity matrix.
3. Search papers by title or keywords.
4. Select a research paper from the search results.
5. Display a preview of the selected paper.
6. Retrieve similarity scores from the similarity matrix.
7. Display the Top-N recommended research papers.

---

## 🔮 Future Improvements

- TF-IDF Vectorizer
- Sentence Transformers (BERT)
- Semantic Search
- FAISS Vector Database
- PDF Upload & Recommendation
- Author-Based Recommendation
- Conference-Based Filtering
- Citation-Based Recommendation
- LLM-Powered Paper Summarization
- Bookmark Favorite Papers
