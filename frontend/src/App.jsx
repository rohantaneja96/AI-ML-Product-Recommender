import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import ChatPage from "./components/ChatPage";
import AnalyticsPage from "./components/AnalyticsPage";

export default function App() {
  return (
    <Router>
      <nav className="bg-blue-700 text-white p-4 flex justify-center gap-10 font-semibold">
        <Link to="/">🏠 Recommend</Link>
        <Link to="/analytics">📊 Analytics</Link>
      </nav>

      <Routes>
        <Route path="/" element={<ChatPage />} />
        <Route path="/analytics" element={<AnalyticsPage />} />
      </Routes>
    </Router>
  );
}
