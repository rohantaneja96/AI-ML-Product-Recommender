from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import recommend,analytics

app = FastAPI(title="AI Product Recommendation API")

# Enable CORS (to connect with React later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(recommend.router)
app.include_router(analytics.router)

@app.get("/")
def root():
    return {"message": "Welcome to AI Product Recommendation API"}

# ✅ This block ensures Render binds to the correct dynamic port
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
