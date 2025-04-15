
import React from 'react';
import Sidebar from './Sidebar';
import Header from './Header';
import Dashboard from './Dashboard';

export default function Layout() {
  return (
    <div className='flex min-h-screen bg-gray-100 dark:bg-gray-900 text-gray-900 dark:text-gray-100'>
      <Sidebar />
      <div className='flex-1 flex flex-col'>
        <Header />
        <main className='p-4'>
          <Dashboard />
        </main>
      </div>
    </div>
  );
}
