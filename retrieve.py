import json
import numpy as np
import faiss
import pickle

with open("data/chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

index = faiss.read_index("data/faiss.index")
X = np.load("data/tfidf.npy")

with open("data/tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

def retrieve(query, k):
    q = vectorizer.transform([query]).astype(np.float32).toarray()
    _, idx = index.search(q, k)
    return [chunks[i] for i in idx[0]]
