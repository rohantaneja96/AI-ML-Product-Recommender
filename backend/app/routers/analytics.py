from fastapi import APIRouter
import pandas as pd
import os

router = APIRouter(prefix="/api", tags=["analytics"])

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", ".."))
DATA_FILE_PATH = os.path.join(BACKEND_DIR, "data", "clean_products.csv")

df = pd.read_csv(DATA_FILE_PATH)

@router.get("/analytics/summary")
def analytics_summary():
    """Return simple analytics stats for dashboard."""
    return {
        "total_products": len(df),
        "unique_categories": df["categories"].nunique(),
        "avg_price": round(df["price"].mean(), 2),
        "top_category": df["categories"].value_counts().idxmax(),
        "materials": df["material"].value_counts().to_dict()
    }
