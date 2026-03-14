import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import Home from './pages/Home';

function App() {
  const [theme, setTheme] = useState('light');

  useEffect(() => {
    const savedTheme = localStorage.getItem('theme') || 'light';
    setTheme(savedTheme);
    document.documentElement.classList.toggle('dark', savedTheme === 'dark');
  }, []);

  const toggleTheme = () => {
    const newTheme = theme === 'light' ? 'dark' : 'light';
    setTheme(newTheme);
    localStorage.setItem('theme', newTheme);
    document.documentElement.classList.toggle('dark', newTheme === 'dark');
  };

  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ duration: 0.5 }}
      className={`min-h-screen ${theme === 'dark' ? 'dark' : ''}`}
    >
      <div className="relative">
        {/* Navigation */}
        <nav className="fixed top-0 left-0 right-0 bg-white dark:bg-gray-900 shadow-md z-50">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="flex justify-between items-center h-16">
              <div className="flex items-center gap-2">
                <div className="text-2xl font-bold text-blue-600">🤖</div>
                <h1 className="text-xl font-bold text-gray-900 dark:text-white">
                  Humanizer
                </h1>
              </div>
              
              <button
                onClick={toggleTheme}
                className="p-2 rounded-lg bg-gray-100 dark:bg-gray-800 text-gray-900 dark:text-gray-100 hover:bg-gray-200 dark:hover:bg-gray-700 transition-colors"
                title="Toggle dark mode"
              >
                {theme === 'light' ? '🌙' : '☀️'}
              </button>
            </div>
          </div>
        </nav>

        {/* Main Content */}
        <main className="pt-16">
          <Home />
        </main>

        {/* Footer */}
        <footer className="bg-gray-900 text-white py-8 mt-16">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-8">
              <div>
                <h3 className="text-lg font-semibold mb-4">About</h3>
                <p className="text-gray-400">
                  Transform AI-generated text into natural, human-like writing.
                </p>
              </div>
              <div>
                <h3 className="text-lg font-semibold mb-4">Features</h3>
                <ul className="text-gray-400 space-y-2">
                  <li>✓ AI Paraphrasing</li>
                  <li>✓ Humanization Engine</li>
                  <li>✓ Grammar Correction</li>
                  <li>✓ Style Adjustment</li>
                </ul>
              </div>
              <div>
                <h3 className="text-lg font-semibold mb-4">Stack</h3>
                <ul className="text-gray-400 space-y-2">
                  <li>React + Tailwind</li>
                  <li>FastAPI</li>
                  <li>HuggingFace</li>
                  <li>PyTorch</li>
                </ul>
              </div>
            </div>
            <div className="border-t border-gray-800 pt-8 text-center text-gray-400">
              <p>&copy; 2024 AI Text to Human Text Converter. Free for everyone.</p>
            </div>
          </div>
        </footer>
      </div>
    </motion.div>
  );
}

export default App;
