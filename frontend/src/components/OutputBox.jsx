import React, { useState } from 'react';
import { motion } from 'framer-motion';

function OutputBox({ value, loading, style, onStyleChange }) {
  const [copied, setCopied] = useState(false);

  const handleCopy = () => {
    navigator.clipboard.writeText(value);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const handleDownload = () => {
    const element = document.createElement('a');
    const file = new Blob([value], { type: 'text/plain' });
    element.href = URL.createObjectURL(file);
    element.download = 'humanized_text.txt';
    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);
  };

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.3, delay: 0.1 }}
      className="w-full"
    >
      <label className="block text-lg font-semibold text-gray-700 dark:text-gray-300 mb-2">
        Humanized Text
      </label>

      <div className="relative">
        <textarea
          value={value}
          readOnly
          placeholder="Your humanized text will appear here..."
          className="w-full h-48 p-4 border-2 border-gray-300 dark:border-gray-600 rounded-lg bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-white placeholder-gray-500 dark:placeholder-gray-400"
        />

        {loading && (
          <div className="absolute inset-0 bg-white/50 dark:bg-gray-800/50 rounded-lg flex items-center justify-center">
            <div className="flex flex-col items-center gap-2">
              <div className="w-8 h-8 border-4 border-gray-300 dark:border-gray-600 border-t-blue-500 dark:border-t-blue-400 rounded-full animate-spin" />
              <p className="text-sm text-gray-600 dark:text-gray-400">Processing...</p>
            </div>
          </div>
        )}
      </div>

      {/* Style selector */}
      <div className="mt-4 flex items-center gap-4">
        <label className="text-sm font-medium text-gray-700 dark:text-gray-300">
          Writing Style:
        </label>
        <select
          value={style}
          onChange={(e) => onStyleChange(e.target.value)}
          className="px-3 py-2 border-2 border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-800 text-gray-900 dark:text-white focus:border-blue-500 dark:focus:border-blue-400 transition-colors"
        >
          <option value="default">Default</option>
          <option value="casual">Casual</option>
          <option value="professional">Professional</option>
          <option value="academic">Academic</option>
          <option value="blog">Blog</option>
        </select>
      </div>

      {/* Action buttons */}
      <div className="flex gap-3 mt-4">
        <motion.button
          whileHover={{ scale: 1.05 }}
          whileTap={{ scale: 0.95 }}
          onClick={handleCopy}
          disabled={!value || loading}
          className={`flex-1 py-2 px-4 rounded-lg font-semibold transition-all ${
            copied
              ? 'bg-green-500 text-white'
              : 'bg-blue-500 hover:bg-blue-600 text-white disabled:opacity-50'
          }`}
        >
          {copied ? '✓ Copied!' : '📋 Copy'}
        </motion.button>

        <motion.button
          whileHover={{ scale: 1.05 }}
          whileTap={{ scale: 0.95 }}
          onClick={handleDownload}
          disabled={!value || loading}
          className="flex-1 py-2 px-4 rounded-lg font-semibold bg-green-500 hover:bg-green-600 text-white transition-all disabled:opacity-50"
        >
          📥 Download
        </motion.button>

        <motion.button
          whileHover={{ scale: 1.05 }}
          whileTap={{ scale: 0.95 }}
          onClick={() => {
            const textarea = document.querySelector('textarea[readonly]');
            const newTab = window.open();
            newTab.document.write(`<pre>${value}</pre>`);
          }}
          disabled={!value || loading}
          className="flex-1 py-2 px-4 rounded-lg font-semibold bg-purple-500 hover:bg-purple-600 text-white transition-all disabled:opacity-50"
        >
          🔗 Share
        </motion.button>
      </div>

      {/* Character count */}
      {value && (
        <div className="mt-4 grid grid-cols-3 gap-4 text-center text-sm">
          <div className="bg-gray-100 dark:bg-gray-800 p-2 rounded">
            <p className="text-gray-600 dark:text-gray-400">Words</p>
            <p className="text-lg font-semibold text-gray-900 dark:text-white">
              {value.split(/\s+/).filter(w => w).length}
            </p>
          </div>
          <div className="bg-gray-100 dark:bg-gray-800 p-2 rounded">
            <p className="text-gray-600 dark:text-gray-400">Characters</p>
            <p className="text-lg font-semibold text-gray-900 dark:text-white">
              {value.length}
            </p>
          </div>
          <div className="bg-gray-100 dark:bg-gray-800 p-2 rounded">
            <p className="text-gray-600 dark:text-gray-400">Sentences</p>
            <p className="text-lg font-semibold text-gray-900 dark:text-white">
              {value.split(/[.!?]+/).filter(s => s.trim()).length}
            </p>
          </div>
        </div>
      )}
    </motion.div>
  );
}

export default OutputBox;
