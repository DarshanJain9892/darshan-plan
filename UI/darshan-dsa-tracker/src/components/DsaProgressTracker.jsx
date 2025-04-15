import React, { useEffect, useState } from 'react';
import { Card, CardContent } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Textarea } from '@/components/ui/textarea';
import { Chart as ChartJS, BarElement, CategoryScale, LinearScale } from 'chart.js';
import { Bar } from 'react-chartjs-2';
import jsPDF from 'jspdf';

ChartJS.register(BarElement, CategoryScale, LinearScale);

const quotes = [
  "Keep going, you're doing great!",
  "Every step counts!",
  "Consistency beats talent!",
  "Push harder than yesterday!",
  "Success is near, stay focused!"
];

const initialTopics = [
  { name: 'Arrays', progress: 80, notes: '', resource: 'https://leetcode.com/tag/array/' },
  { name: 'Strings', progress: 60, notes: '', resource: 'https://leetcode.com/tag/string/' },
  { name: 'Linked List', progress: 40, notes: '', resource: 'https://leetcode.com/tag/linked-list/' },
  { name: 'Stack & Queue', progress: 30, notes: '', resource: 'https://leetcode.com/tag/stack/' },
  { name: 'Trees', progress: 20, notes: '', resource: 'https://leetcode.com/tag/tree/' },
  { name: 'Graphs', progress: 10, notes: '', resource: 'https://leetcode.com/tag/graph/' },
  { name: 'Dynamic Programming', progress: 0, notes: '', resource: 'https://leetcode.com/tag/dynamic-programming/' }
];

export default function DsaProgressTracker() {
  const [topics, setTopics] = useState(() => JSON.parse(localStorage.getItem('dsaProgress')) || initialTopics);
  const [quote, setQuote] = useState('');

  useEffect(() => {
    setQuote(quotes[Math.floor(Math.random() * quotes.length)]);
  }, []);

  useEffect(() => {
    localStorage.setItem('dsaProgress', JSON.stringify(topics));
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

  const downloadPDF = () => {
    const doc = new jsPDF();
    doc.text("Darshan's DSA Progress Tracker", 10, 10);
    topics.forEach((topic, idx) => {
      doc.text(`${idx + 1}. ${topic.name} - ${topic.progress}%`, 10, 20 + idx * 10);
    });
    doc.save('Darshan_DSA_Progress.pdf');
  };

  const averageProgress = Math.round(topics.reduce((acc, t) => acc + t.progress, 0) / topics.length);

  const chartData = {
    labels: topics.map(t => t.name),
    datasets: [
      {
        label: 'Progress %',
        data: topics.map(t => t.progress),
        backgroundColor: 'rgba(75, 192, 192, 0.5)',
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1
      }
    ]
  };

  return (
    <div className="p-6 max-w-5xl mx-auto">
      <div className="text-center mb-6">
        <h1 className="text-4xl font-bold mb-2">Darshan's DSA Progress Tracker</h1>
        <p className="text-gray-600 mb-4">Track your journey to become DSA Pro!</p>
        <h2 className="mb-4">Motivation: {quote}</h2>
        <h2 className="mb-4">Overall Completion: {averageProgress}%</h2>
        <Button onClick={downloadPDF} className="mr-2">Download as PDF</Button>
        <Button onClick={() => window.print()}>Print Progress</Button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {topics.map((topic, index) => (
          <Card key={index}>
            <CardContent className="flex flex-col gap-2">
              <h2 className="text-xl font-semibold">{topic.name}</h2>
              <a href={topic.resource} target="_blank" rel="noopener noreferrer" className="text-blue-500 underline">Resources</a>
              <Input type="number" value={topic.progress} min="0" max="100" onChange={(e) => updateProgress(index, e.target.value)} />
              <Textarea value={topic.notes} onChange={(e) => updateNotes(index, e.target.value)} placeholder="Write notes here..." />
            </CardContent>
          </Card>
        ))}
      </div>

      <div className="mt-8">
        <Bar data={chartData} />
      </div>
    </div>
  );
}
