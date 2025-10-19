import { useEffect, useState } from "react";
import { getAnalytics } from "../api/api";

export default function AnalyticsPage() {
  const [data, setData] = useState(null);

  useEffect(() => {
    getAnalytics().then(setData);
  }, []);

  if (!data) return <div className="text-center mt-20 text-lg">Loading analytics...</div>;

  return (
    <div className="min-h-screen bg-gray-50 flex flex-col items-center justify-center p-6">
      <h1 className="text-3xl font-bold mb-6 text-blue-700">📊 Dataset Analytics</h1>
      <div className="grid grid-cols-2 md:grid-cols-3 gap-6 max-w-4xl w-full">
        <div className="bg-white shadow-md p-4 rounded-xl text-center">
          <h2 className="text-xl font-semibold">Total Products</h2>
          <p className="text-2xl font-bold text-blue-600">{data.total_products}</p>
        </div>
        <div className="bg-white shadow-md p-4 rounded-xl text-center">
          <h2 className="text-xl font-semibold">Unique Categories</h2>
          <p className="text-2xl font-bold text-blue-600">{data.unique_categories}</p>
        </div>
        <div className="bg-white shadow-md p-4 rounded-xl text-center">
          <h2 className="text-xl font-semibold">Average Price</h2>
          <p className="text-2xl font-bold text-blue-600">₹{data.avg_price}</p>
        </div>
      </div>

      <div className="mt-10 bg-white p-6 rounded-2xl shadow-lg max-w-2xl w-full">
        <h3 className="text-lg font-semibold mb-4 text-blue-600">Material Distribution</h3>
        {Object.entries(data.materials).map(([mat, count]) => (
          <p key={mat} className="text-gray-700">{mat}: {count}</p>
        ))}
      </div>
    </div>
  );
}
