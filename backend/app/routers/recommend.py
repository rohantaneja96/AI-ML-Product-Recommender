import os
from fastapi import APIRouter
import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from functools import lru_cache
from difflib import get_close_matches
from app.utils.genai import generate_creative_description

router = APIRouter(prefix="/api", tags=["recommendations"])

# ✅ Absolute paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))       # app/routers
BACKEND_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", ".."))  # backend

# ✅ Load dataset
DATA_FILE_PATH = os.path.join(BACKEND_DIR, "data", "clean_products.csv")
df = pd.read_csv(DATA_FILE_PATH)
df.columns = [c.strip().lower() for c in df.columns]  # normalize column names

# ✅ FAISS index file path
INDEX_FILE_PATH = os.path.join(BACKEND_DIR, "app", "models", "vector_store", "products.index")

# ✅ Cache model and FAISS index so they load only once
@lru_cache(maxsize=1)
def get_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

@lru_cache(maxsize=1)
def get_index():
    if not os.path.exists(INDEX_FILE_PATH):
        raise FileNotFoundError("❌ FAISS index not found. Run embeddings.py first.")
    return faiss.read_index(INDEX_FILE_PATH)

# ✅ Load them once (cached)
model = get_model()
index = get_index()

@router.get("/recommend")
def recommend_product(title: str):
    try:
        # 1️⃣ Try to find close matches (case-insensitive + partial)
        matches = df[df['title'].str.lower().str.contains(title.lower(), na=False)]

        if matches.empty:
            # If nothing matches even partially
            return {"error": f"No products found matching '{title}'."}

        # Pick the first close match
        item = matches.iloc[0]

        # 2️⃣ Use clean description
        item_desc = str(item.get('description', ''))

        # 3️⃣ Create embedding + find similar products
        query_embedding = model.encode([item_desc])
        D, I = index.search(np.array(query_embedding).astype("float32"), k=5)

        recommendations = []
        for idx in I[0]:
            rec_item = df.iloc[idx].to_dict()

            # ✅ Replace NaN with empty strings
            for key, value in rec_item.items():
                if pd.isna(value):
                    rec_item[key] = ""

            # ✅ Generate creative description safely
            try:
                rec_item["creative_description"] = generate_creative_description(
                    str(rec_item.get("description", "")),
                    str(rec_item.get("categories", "")),
                )
            except Exception as e:
                rec_item["creative_description"] = f"[GenAI error: {str(e)}]"

            recommendations.append(rec_item)

        return {
            "query": title,
            "matched_product": item['title'],
            "recommendations": recommendations
        }

    except Exception as e:
        return {"error": str(e)}

