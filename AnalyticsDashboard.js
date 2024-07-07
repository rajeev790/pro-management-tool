import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import axios from 'axios';

const AnalyticsDashboard = () => {
  const [chartData, setChartData] = useState({});

  useEffect(() => {
    const fetchData = async () => {
      const result = await axios.get('/analytics');
      setChartData(result.data);
    };
    fetchData();
  }, []);

  return (
    <div>
      <h1>Analytics Dashboard</h1>
      <Line data={chartData} />
    </div>
  );
};

export default AnalyticsDashboard;