import json
import numpy as np
import faiss
from sklearn.feature_extraction.text import TfidfVectorizer

print("[LOAD] Loading chunks...")
with open("data/chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

texts = [c["text"] for c in chunks]
print(f"[INFO] Chunks: {len(texts)}")

print("[TFIDF] Vectorizing...")
vectorizer = TfidfVectorizer(
    max_features=50000, ngram_range=(1, 2), stop_words="english"
)

X = vectorizer.fit_transform(texts).astype(np.float32)

print("[FAISS] Building index...")
index = faiss.IndexFlatIP(X.shape[1])
index.add(X.toarray())

faiss.write_index(index, "data/faiss.index")
np.save("data/tfidf.npy", X.toarray())

import pickle

with open("data/tfidf_vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("[DONE] TF-IDF index created")
