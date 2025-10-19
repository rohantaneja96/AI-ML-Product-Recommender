import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os

# Get absolute path to backend folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # app/utils
BACKEND_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", ".."))  # backend

# Load dataset
df = pd.read_csv(os.path.join(BACKEND_DIR, "data", "clean_products.csv"))

# Create embeddings folder
VECTOR_STORE_DIR = os.path.join(BACKEND_DIR, "app", "models", "vector_store")
os.makedirs(VECTOR_STORE_DIR, exist_ok=True)

# Load pre-trained embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate embeddings for product descriptions
embeddings = model.encode(df["clean_description"].tolist())

# Store in FAISS
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings).astype("float32"))

# Absolute path for FAISS index file
INDEX_FILE_PATH = os.path.join(VECTOR_STORE_DIR, "products.index")
faiss.write_index(index, INDEX_FILE_PATH)

print(f"✅ Vector store created successfully at: {INDEX_FILE_PATH}")
