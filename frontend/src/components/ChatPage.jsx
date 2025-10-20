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
      if (data.error) setError(data.error);
      else setRecommendations(data.recommendations);
    } catch (err) {
      setError("⚠️ Backend not responding. Please check your FastAPI server.");
    }
    setLoading(false);
  };

  return (
    <div className="min-h-screen flex flex-col bg-gradient-to-br from-indigo-700 via-purple-700 to-pink-600 relative text-white overflow-hidden">

      {/* 🌈 Animated Marquee Header */}
      <div className="absolute top-6 text-center w-full">
        <marquee
          behavior="alternate"
          scrollamount="6"
          className="text-3xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-yellow-300 via-pink-300 to-purple-400 drop-shadow-md"
        >
          ✨ Welcome to the Smart AI Furniture Recommender ✨
        </marquee>
        <marquee
          behavior="alternate"
          direction="left"
          scrollamount="4"
          className="text-lg font-semibold text-transparent bg-clip-text bg-gradient-to-r from-indigo-200 via-pink-100 to-yellow-200 italic mt-1"
        >
          🪑 Discover beautiful, intelligent furniture picks powered by AI!
        </marquee>
      </div>

      {/* 💎 Perfectly Centered Search Box */}
      <div className="flex items-center justify-center min-h-screen px-4">
        <div className="bg-white/20 backdrop-blur-2xl border border-white/40 rounded-3xl shadow-2xl p-10 w-full max-w-lg text-center transform hover:scale-[1.02] transition-all duration-300">
          <h1 className="text-3xl font-bold text-yellow-200 mb-6">
            🔍 AI Product Search
          </h1>

          {/* 🧭 Search Form */}
          <form onSubmit={handleSubmit} className="flex flex-col items-center gap-4 w-full">
            <div className="w-full bg-white rounded-2xl shadow-inner border border-gray-300 focus-within:ring-4 focus-within:ring-pink-400 transition-all">
              <input
                type="text"
                className="w-full p-4 text-gray-800 text-lg rounded-2xl outline-none placeholder-gray-500 text-center"
                placeholder="Enter product name:-"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
              />
            </div>

            <button
              type="submit"
              className="w-1/2 py-3 bg-gradient-to-r from-pink-500 to-purple-600 text-white font-semibold rounded-2xl shadow-lg hover:scale-105 transition-transform"
            >
              {loading ? "⏳ Searching..." : "✨ Get Recommendations"}
            </button>
          </form>

          {/* ⚠️ Error Display */}
          {error && (
            <p className="text-red-700 bg-white/80 p-2 mt-4 rounded-lg font-medium animate-pulse">
              {error}
            </p>
          )}

          {/* 💬 Message */}
          {!loading && recommendations.length === 0 && !error && (
            <p className="text-white mt-6 text-lg italic animate-pulse">
              Try searching for your favorite furniture above 💫
            </p>
          )}
        </div>
      </div>

      {/* 🪄 Recommendations Section */}
      <div className="w-full max-w-6xl mx-auto mt-12 grid gap-8 sm:grid-cols-2 lg:grid-cols-3 px-4 pb-10">
        {recommendations.map((rec, index) => (
          <div
            key={index}
            className="bg-white/80 backdrop-blur-md rounded-3xl shadow-xl hover:shadow-pink-300 border border-gray-200 p-5 transform hover:-translate-y-1 transition-all duration-300"
          >
            <img
              src={rec.images || rec.image || 'https://via.placeholder.com/250'}
              alt={rec.title}
              className="w-full h-52 object-cover rounded-2xl mb-4"
            />
            <h2 className="text-xl font-bold text-indigo-700">{rec.title}</h2>
            <p className="text-gray-500 mb-1">{rec.brand}</p>
            <p className="text-gray-700 text-sm mb-3 line-clamp-3">
              {rec.description}
            </p>
            <p className="text-pink-600 font-medium italic">
              ✨ {rec.creative_description}
            </p>
          </div>
        ))}
      </div>

      {/* 🌊 Animated background glow (premium effect) */}
      <div className="absolute inset-0 -z-10 bg-gradient-to-r from-indigo-600 via-purple-600 to-pink-500 animate-[gradient_10s_ease_infinite] opacity-60"></div>
    </div>
  );
}
