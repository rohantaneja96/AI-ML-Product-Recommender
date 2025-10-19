# 🛋️ AI Product Recommendation System

A smart AI-powered recommendation system that suggests similar furniture products and generates premium marketing descriptions using **Gemini + FAISS + Sentence Transformers + FastAPI + React (Vite + Tailwind)**.

This system takes a product title as input and returns:
- Top similar product recommendations (via embeddings + FAISS)
- Original product details
- AI-generated creative marketing descriptions (via Google Gemini)

🚀 **Live Frontend:** https://ai-ml-product-recommender.vercel.app  
🌐 **Live Backend (API):** https://<your-backend-url>.onrender.com *(To be updated after Render deployment)*

---

## ✅ Features

| Feature | Description |
|---------|------------|
| 🔍 Semantic Product Search | Finds similar products using embeddings |
| 🧠 AI Creative Descriptions | Gemini generates short premium marketing text |
| ⚡ Fast Recommendation Engine | FAISS vector similarity search |
| 🌐 Full-Stack System | FastAPI backend + React frontend |
| 📦 Small Custom Dataset | 50 furniture products (CSV) |
| 🎨 Clean Modern UI | Built using React + Tailwind |

---

## 🏗️ Tech Stack

**Frontend:** React (Vite), TailwindCSS  
**Backend:** FastAPI, Uvicorn, Python  
**AI / ML:**  
- Sentence Transformer: `all-MiniLM-L6-v2` (embeddings)  
- FAISS (vector similarity search)  
- Google Gemini (text generation)

**Data:** Custom CSV dataset (`clean_products.csv`)

**Deployment:**  
- Backend → Render  
- Frontend → Vercel

---

## 🔄 System Architecture

User (React UI)
│
▼
Frontend (Vercel) ───────► Backend (Render / FastAPI)
│
├── Gemini (Creative Text)
├── SentenceTransformer (Embeddings)
└── FAISS (Vector Search)


---

## 📌 How It Works (Simple Flow)

1. User searches **“HomeLuxe Wood Chair”**
2. Frontend calls backend: `/api/recommend?title=<query>`
3. Backend finds product in CSV + embeds its description
4. FAISS finds top 5 similar products
5. Gemini generates creative 2-line marketing descriptions
6. Response sent back to UI
7. UI displays **cards with image, details, and AI description**

---

🛠️ Local Development (Run on your laptop)

✅ Backend (FastAPI)

cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

Now open: http://127.0.0.1:8000

### ✅ Frontend (React + Vite)

cd frontend
npm install
npm run dev

Now open: http://127.0.0.1:5173

---

## 📌 API Example

**Endpoint:**


**Response:**

{
"query": "HomeLuxe Wood Chair",
"recommendations": [ ... ]
}


---

## 📸 Screenshots (add later)

- 🖼️ Home Page
- 🖼️ Recommendation Output
- 🖼️ Analytics Page

---

## 🚀 Deployment Plan (2 URLs)

| Service | Platform | Output |
|----------|----------|---------|
| Backend | Render | https://your-backend.onrender.com |
| Frontend | Vercel | https://ai-ml-product-recommender.vercel.app |

---

## 🧠 Future Improvements (for interview discussion)

- ✅ Add login & personalization
- ✅ Add product ratings & reviews
- ✅ Cache AI descriptions (reduce cost)
- ✅ Add database (PostgreSQL / MongoDB)
- ✅ Add recommendation analytics dashboard

---

## 👤 Author
**Built by _Rohan Taneja_**

---

