# 🔍 AI Research Paper Intelligence System

An AI-powered research paper search engine that enables users to semantically search research papers, generate AI-based summaries, extract important keywords, and discover related papers.

Built using NLP, Sentence Transformers, FAISS, Streamlit, and Hugging Face Transformers.

---

## 🚀 Features

- 🔎 Semantic Search using Sentence Transformers
- 🤖 AI-generated Paper Summaries
- 🏷️ Automatic Keyword Extraction
- 📚 Research Paper Recommendations
- 🎨 Modern Streamlit User Interface
- ⚡ Fast similarity search using FAISS

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Sentence Transformers
- FAISS
- Hugging Face Transformers
- KeyBERT
- Pandas
- NumPy
- Scikit-learn

---

## 📂 Project Structure

```
AI-Research-Paper-Search-Engine/
│
├── src/
│   ├── app.py
│   ├── search_engine.py
│   ├── build_index.py
│   └── data_prep.py
│
├── Search_Engine.ipynb
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Chaitanyapakhare7/AI-Research-Paper-Search-Engine.git
```

Move into the project directory

```bash
cd AI-Research-Paper-Search-Engine
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run src/app.py
```

---

## 💡 How It Works

1. User enters a research topic.
2. The query is converted into embeddings using Sentence Transformers.
3. FAISS retrieves the most relevant research papers.
4. A Transformer model generates concise summaries.
5. KeyBERT extracts the most relevant keywords.
6. Similar research papers are recommended.

---

## 📸 Demo

Features included:

- Semantic Research Paper Search
- AI Summary Generation
- Keyword Extraction
- Research Paper Recommendations
- Interactive Streamlit Dashboard

---

## 🎯 Future Improvements

- Named Entity Recognition (NER)
- PDF Upload & Analysis
- Citation Network Visualization
- Research Trend Analysis
- Paper Chat Assistant

---

## 👨‍💻 Author

**Chaitanya Pakhare**

Walchand College of Engineering, Sangli

---
