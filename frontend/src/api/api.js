import axios from "axios";

const API_BASE = "http://127.0.0.1:8000/api";

export const getRecommendations = async (title) => {
  const response = await axios.get(`${API_BASE}/recommend`, {
    params: { title },
  });
  return response.data;
};

export const getAnalytics = async () => {
  const response = await axios.get(`${API_BASE}/analytics/summary`);
  return response.data;
};
