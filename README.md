# 📚 Research Paper Recommendation System

A Machine Learning project that recommends research papers based on their textual content using **Natural Language Processing (NLP)** and **Content-Based Filtering**.

The system analyzes research paper abstracts and titles, converts them into numerical vectors, and recommends the most similar papers using **Cosine Similarity**.

---

---

## 🚀 Features

- 📄 Content-Based Research Paper Recommendation
- 🧹 NLP Text Preprocessing
- 🔤 CountVectorizer for Feature Extraction
- 📊 Cosine Similarity for Recommendations
- 💾 Pickle Support for Model Saving
- ⚡ Fast Recommendation Generation

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- CountVectorizer
- Cosine Similarity
- Pickle
- Jupyter Notebook

---

## 📂 Dataset

This project uses the **NIPS Research Papers Dataset**, which contains:

- Research Paper Title
- Abstract
- Full Paper Text
- Publication Year
- Event Type

---

## 📁 Project Structure

```
Research-Paper-Recommendation-System/
│
├── researchpaper.ipynb
├── paper.pkl
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Research-Paper-Recommendation-System.git
```

Go to the project directory:

```bash
cd Research-Paper-Recommendation-System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Launch Jupyter Notebook:

```bash
jupyter notebook
```

---

## 🔄 Workflow

1. Load the dataset
2. Perform text preprocessing
3. Remove stopwords and punctuation
4. Apply lemmatization
5. Convert text into vectors using CountVectorizer
6. Compute Cosine Similarity
7. Recommend the most relevant research papers

---

## 💡 Example

### Input

```
Deep Learning
```

### Output

```
1. Deep Learning for Computer Vision
2. Deep Neural Networks for Image Classification
3. Representation Learning using Deep Models
4. Convolutional Neural Networks Explained
5. Advances in Deep Learning
```

---

## 🔮 Future Improvements

- TF-IDF Vectorizer
- Sentence Transformers (BERT)
- FAISS for Large-Scale Search
- Streamlit Web Application
- PDF Recommendation Support
- Semantic Search using Embeddings

---

## 🤝 Contributing

Contributions are welcome.

1. Fork this repository
2. Create a new branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## 📜 License

This project is released under the MIT License.

---

## 👨‍💻 Author

**Malkit Choudhary**

- Data Science Enthusiast
- Machine Learning Developer
- Python Programmer

⭐ If you found this project useful, please consider giving it a **star**.
