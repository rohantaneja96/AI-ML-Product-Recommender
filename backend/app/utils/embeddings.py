import os
import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# ✅ Paths setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))       # app/utils
BACKEND_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", ".."))  # backend

DATA_FILE_PATH = os.path.join(BACKEND_DIR, "data", "clean_products.csv")
VECTOR_STORE_DIR = os.path.join(BACKEND_DIR, "app", "models", "vector_store")
os.makedirs(VECTOR_STORE_DIR, exist_ok=True)

INDEX_FILE_PATH = os.path.join(VECTOR_STORE_DIR, "products.index")

# ✅ Step 1: Load dataset
print("📦 Loading dataset...")
df = pd.read_csv(DATA_FILE_PATH)
df.columns = [c.strip().lower() for c in df.columns]

if "description" not in df.columns:
    raise ValueError("❌ 'description' column not found in dataset!")

# ✅ Step 2: Prepare text data
df["description"] = df["description"].astype(str).fillna("")
descriptions = df["description"].tolist()

# ✅ Step 3: Load embedding model
print("🧠 Loading SentenceTransformer model (all-MiniLM-L6-v2)...")
model = SentenceTransformer("all-MiniLM-L6-v2")

# ✅ Step 4: Generate embeddings
print("⚙️ Generating embeddings for products...")
embeddings = model.encode(descriptions, show_progress_bar=True)

# ✅ Step 5: Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings).astype("float32"))

# ✅ Step 6: Save index
faiss.write_index(index, INDEX_FILE_PATH)
print(f"✅ Vector store created successfully at: {INDEX_FILE_PATH}")
