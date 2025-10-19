import { useState } from "react";

const API_URL = "http://127.0.0.1:8000/api/recommend"; // ✅ Backend URL

export default function ChatPage() {
  const [query, setQuery] = useState("");
  const [recommendations, setRecommendations] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!query.trim()) return;

    setLoading(true);
    setRecommendations([]);
    setError(null);

    try {
      const response = await fetch(`${API_URL}?title=${encodeURIComponent(query)}`);
      const data = await response.json();

      if (data.error) {
        setError(data.error);
      } else {
        setRecommendations(data.recommendations);
      }

    } catch (err) {
      setError("Backend not responding. Please check your FastAPI server.");
    }

    setLoading(false);
  };

  return (
    <div className="flex flex-col items-center p-10">
      <h1 className="text-3xl font-bold mb-5">🪑 AI Furniture Recommender</h1>

      <form onSubmit={handleSubmit} className="flex gap-2 w-full max-w-lg">
        <input
          type="text"
          className="flex-1 p-3 rounded-lg border border-gray-300 shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-400"
          placeholder="Enter product title (e.g. HomeLuxe Wood Chair)"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />

        <button
          type="submit"
          className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition"
        >
          {loading ? "Thinking..." : "Search"}
        </button>
      </form>

      {error && <p className="text-red-600 mt-4">{error}</p>}

      <div className="w-full max-w-2xl mt-8">
        {recommendations.map((rec, index) => (
          <div key={index} className="p-4 mb-4 border rounded-lg shadow-sm bg-white">
            <h2 className="text-xl font-bold">{rec.title}</h2>
            <p className="text-gray-700">{rec.description}</p>
            <p className="text-blue-600 mt-1 font-semibold">
              ✨ {rec.creative_description}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}
