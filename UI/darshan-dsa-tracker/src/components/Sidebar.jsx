
import React from 'react';

export default function Sidebar() {
  return (
    <div className='w-60 bg-gray-800 text-white p-4 hidden md:block'>
      <h2 className='text-2xl font-bold mb-6'>Darshan</h2>
      <ul className='space-y-4'>
        <li className='hover:text-gray-400 cursor-pointer'>Dashboard</li>
        <li className='hover:text-gray-400 cursor-pointer'>Topics</li>
        <li className='hover:text-gray-400 cursor-pointer'>Analytics</li>
        <li className='hover:text-gray-400 cursor-pointer'>Settings</li>
      </ul>
    </div>
  );
}
