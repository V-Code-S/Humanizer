import React, { useState } from 'react';
import { motion } from 'framer-motion';

function InputBox({ value, onChange, placeholder, label, maxLength }) {
  const charCount = value.length;
  const percentage = (charCount / maxLength) * 100;

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.3 }}
      className="w-full"
    >
      <label className="block text-lg font-semibold text-gray-700 dark:text-gray-300 mb-2">
        {label}
      </label>
      
      <div className="relative">
        <textarea
          value={value}
          onChange={(e) => onChange(e.target.value)}
          placeholder={placeholder}
          maxLength={maxLength}
          className="w-full h-48 p-4 border-2 border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-800 text-gray-900 dark:text-white placeholder-gray-500 dark:placeholder-gray-400 focus:border-blue-500 dark:focus:border-blue-400 transition-colors"
        />
        
        {/* Character count progress bar */}
        <div className="absolute bottom-0 left-0 right-0 h-1 bg-gray-200 dark:bg-gray-700 rounded-b-lg overflow-hidden">
          <motion.div
            initial={{ width: 0 }}
            animate={{ width: `${percentage}%` }}
            className={`h-full transition-colors ${
              percentage > 80
                ? 'bg-red-500'
                : percentage > 60
                ? 'bg-yellow-500'
                : 'bg-green-500'
            }`}
          />
        </div>
      </div>

      <div className="flex justify-between items-center mt-2 text-sm text-gray-500 dark:text-gray-400">
        <span>Maximum characters: {maxLength}</span>
        <span className="font-semibold">
          {charCount} / {maxLength}
        </span>
      </div>
    </motion.div>
  );
}

export default InputBox;
