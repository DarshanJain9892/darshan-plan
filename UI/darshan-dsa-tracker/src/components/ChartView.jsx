import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

import React from 'react';
import { Bar } from 'react-chartjs-2';

export default function ChartView({ topics }) {
  const data = {
    labels: topics.map(topic => topic.name),
    datasets: [{
      label: 'Progress %',
      data: topics.map(topic => topic.progress),
      backgroundColor: 'rgba(75,192,192,0.6)',
    }],
  };

  return (
    <div className='bg-white dark:bg-gray-700 p-4 rounded shadow'>
      <Bar data={data} />
    </div>
  );
}
