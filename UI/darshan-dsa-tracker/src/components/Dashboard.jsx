
import React, { useState, useEffect } from 'react';
import ChartView from './ChartView';

const initialTopics = [
  { name: 'Arrays', progress: 80, notes: '' },
  { name: 'Strings', progress: 60, notes: '' },
  { name: 'Trees', progress: 40, notes: '' },
  { name: 'Graphs', progress: 30, notes: '' },
];

export default function Dashboard() {
  const [topics, setTopics] = useState(() => JSON.parse(localStorage.getItem('topics')) || initialTopics);
  const [tempInputs, setTempInputs] = useState(() => topics.map(topic => topic.progress.toString()));

  useEffect(() => {
    localStorage.setItem('topics', JSON.stringify(topics));
  }, [topics]);

  const updateProgress = (index, value) => {
    const updated = [...topics];
    updated[index].progress = parseInt(value) || 0;
    setTopics(updated);
  };

  const updateNotes = (index, value) => {
    const updated = [...topics];
    updated[index].notes = value;
    setTopics(updated);
  };

  return (
    <div>
      <h2 className='text-2xl font-bold mb-4'>Welcome, Darshan!</h2>
      <ChartView topics={topics} />
      <div className='mt-8 grid grid-cols-1 md:grid-cols-2 gap-4'>
        {topics.map((topic, index) => (
          <div key={index} className='bg-white dark:bg-gray-700 p-4 rounded shadow'>
            <h3 className='font-semibold text-lg mb-2'>{topic.name}</h3>
            <input
              type='number'
              value={tempInputs[index]}
              onChange={(e) => {
                const updated = [...tempInputs];
                updated[index] = e.target.value;
                setTempInputs(updated);
              }}
              onKeyDown={(e) => {
                if (e.key === 'Enter') {
                  updateProgress(index, tempInputs[index]);
                }
              }}
              className='border p-2 rounded w-full mb-2'
            />
            <textarea
              value={topic.notes}
              onChange={(e) => updateNotes(index, e.target.value)}
              placeholder='Add your notes...'
              className='border p-2 rounded w-full'
            />
          </div>
        ))}
      </div>
    </div>
  );
}
