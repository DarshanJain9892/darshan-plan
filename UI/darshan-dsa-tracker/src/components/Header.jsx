
import React, { useState } from 'react';

export default function Header() {
  const [dark, setDark] = useState(false);

  const toggleDarkMode = () => {
    document.documentElement.classList.toggle('dark');
    setDark(!dark);
  };

  return (
    <header className='flex justify-between items-center p-4 bg-white dark:bg-gray-800 shadow'>
      <h1 className='text-xl font-bold'>DSA Progress Tracker</h1>
      <button onClick={toggleDarkMode} className='bg-gray-700 text-white px-4 py-2 rounded'>
        {dark ? 'Light Mode' : 'Dark Mode'}
      </button>
    </header>
  );
}
