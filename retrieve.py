import json
import pickle
import faiss
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


def load_chunks():
    with open("data/chunks.json", "r", encoding="utf-8") as f:
        return json.load(f)


def retrieve(query, top_k=5):
    chunks = load_chunks()

    vectorizer = pickle.load(open("data/tfidf_vectorizer.pkl", "rb"))
    index = faiss.read_index("data/faiss.index")

    q_vec = vectorizer.transform([query]).toarray().astype("float32")
    _, ids = index.search(q_vec, top_k)

    results = []
    for idx in ids[0]:
        if idx < len(chunks):
            results.append(chunks[idx])

    return results
