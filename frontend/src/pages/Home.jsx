import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import InputBox from '../components/InputBox';
import OutputBox from '../components/OutputBox';
import HumanizeButton from '../components/HumanizeButton';
import api, { API_BASE_URL } from '../api';

function Home() {
  const [inputText, setInputText] = useState('');
  const [outputText, setOutputText] = useState('');
  const [loading, setLoading] = useState(false);
  const [style, setStyle] = useState('default');
  const [error, setError] = useState('');
  const [stats, setStats] = useState(null);
  const [apiHealthy, setApiHealthy] = useState(true);

  // Check API health on mount
  useEffect(() => {
    checkApiHealth();
  }, []);

  const checkApiHealth = async () => {
    try {
      const healthy = await api.healthCheck();
      setApiHealthy(healthy);
    } catch {
      setApiHealthy(false);
    }
  };

  const handleHumanize = async () => {
    if (!inputText.trim()) {
      setError('Please enter some text to humanize');
      return;
    }

    if (inputText.length < 10) {
      setError('Text must be at least 10 characters long');
      return;
    }

    setLoading(true);
    setError('');

    try {
      const response = await api.humanizeText(inputText, style);
      setOutputText(response.humanized_text);
      
      // Update stats
      setStats({
        processingTime: response.processing_time,
        originalLength: response.original_text.length,
        humanizedLength: response.humanized_text.length,
      });
    } catch (err) {
      setError(err.message || 'Failed to humanize text. Please try again.');
      console.error('Humanization error:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleClear = () => {
    setInputText('');
    setOutputText('');
    setError('');
    setStats(null);
  };

  const handleStyleChange = async () => {
    if (outputText && inputText) {
      setLoading(true);
      try {
        const response = await api.humanizeText(inputText, style);
        setOutputText(response.humanized_text);
      } catch (err) {
        setError('Failed to apply style. Please try again.');
      } finally {
        setLoading(false);
      }
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 dark:from-gray-900 dark:to-gray-800">
      <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        {/* Header */}
        <motion.div
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
          className="text-center mb-12"
        >
          <h1 className="text-5xl font-bold text-gray-900 dark:text-white mb-4">
            AI Text → Human Text
          </h1>
          <p className="text-xl text-gray-600 dark:text-gray-300">
            Transform AI-generated text into natural, human-like writing
          </p>
          <p className="text-gray-500 dark:text-gray-400 mt-2">
            Free alternative to Undetectable AI, Quillbot, and HumanizeAI
          </p>
        </motion.div>

        {/* API Health Alert */}
        {!apiHealthy && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            className="mb-6 p-4 bg-yellow-100 dark:bg-yellow-900 border-l-4 border-yellow-500 rounded-lg"
          >
            <p className="text-sm text-yellow-800 dark:text-yellow-200">
              ⚠️ Backend API is not responding at {API_BASE_URL}.
            </p>
          </motion.div>
        )}

        {/* Error Alert */}
        {error && (
          <motion.div
            initial={{ opacity: 0, y: -10 }}
            animate={{ opacity: 1, y: 0 }}
            className="mb-6 p-4 bg-red-100 dark:bg-red-900 border-l-4 border-red-500 rounded-lg"
          >
            <p className="text-sm text-red-800 dark:text-red-200">{error}</p>
          </motion.div>
        )}

        {/* Main Container */}
        <div className="bg-white dark:bg-gray-800 rounded-xl shadow-2xl p-8">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
            {/* Left Column - Input */}
            <InputBox
              value={inputText}
              onChange={setInputText}
              placeholder="Paste your AI-generated text here. Minimum 10 characters..."
              label="AI-Generated Text"
              maxLength={5000}
            />

            {/* Right Column - Output */}
            <OutputBox
              value={outputText}
              loading={loading}
              style={style}
              onStyleChange={setStyle}
            />
          </div>

          {/* Action Buttons */}
          <div className="flex flex-col gap-4 mt-8">
            <HumanizeButton
              onClick={handleHumanize}
              loading={loading}
              disabled={!inputText.trim() || !apiHealthy}
            />

            <div className="flex gap-4">
              <motion.button
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                onClick={handleClear}
                className="flex-1 py-2 px-4 bg-gray-100 hover:bg-gray-200 dark:bg-gray-700 dark:hover:bg-gray-600 text-gray-900 dark:text-white rounded-lg font-semibold transition-colors"
              >
                🔄 Clear All
              </motion.button>

              <motion.button
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                onClick={() => {
                  setInputText(outputText);
                  setOutputText('');
                }}
                disabled={!outputText}
                className="flex-1 py-2 px-4 bg-indigo-100 hover:bg-indigo-200 dark:bg-indigo-900 dark:hover:bg-indigo-800 text-indigo-900 dark:text-indigo-100 rounded-lg font-semibold transition-colors disabled:opacity-50"
              >
                ↻ Use Output as Input
              </motion.button>
            </div>
          </div>

          {/* Stats */}
          {stats && (
            <motion.div
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              className="mt-8 p-4 bg-blue-50 dark:bg-blue-900/20 rounded-lg"
            >
              <div className="grid grid-cols-3 gap-4 text-center text-sm">
                <div>
                  <p className="text-gray-600 dark:text-gray-400">Processing Time</p>
                  <p className="text-lg font-semibold text-blue-600 dark:text-blue-400">
                    {stats.processingTime}s
                  </p>
                </div>
                <div>
                  <p className="text-gray-600 dark:text-gray-400">Original</p>
                  <p className="text-lg font-semibold text-gray-900 dark:text-white">
                    {stats.originalLength} chars
                  </p>
                </div>
                <div>
                  <p className="text-gray-600 dark:text-gray-400">Humanized</p>
                  <p className="text-lg font-semibold text-gray-900 dark:text-white">
                    {stats.humanizedLength} chars
                  </p>
                </div>
              </div>
            </motion.div>
          )}
        </div>

        {/* Features Section */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2 }}
          className="mt-12"
        >
          <h2 className="text-3xl font-bold text-gray-900 dark:text-white mb-8 text-center">
            Features
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            {[
              {
                icon: '🤖',
                title: 'AI Paraphrasing',
                desc: 'Rewrite text using advanced transformer models',
              },
              {
                icon: '🎨',
                title: 'Humanization',
                desc: 'Add natural variation and human touch',
              },
              {
                icon: '✍️',
                title: 'Grammar Fix',
                desc: 'Automatic grammar and spell checking',
              },
              {
                icon: '🎯',
                title: 'Style Options',
                desc: 'Choose casual, professional, or academic',
              },
            ].map((feature, idx) => (
              <motion.div
                key={idx}
                whileHover={{ translateY: -5 }}
                className="bg-gradient-to-br from-white to-gray-50 dark:from-gray-800 dark:to-gray-900 p-6 rounded-lg shadow-lg"
              >
                <div className="text-4xl mb-3">{feature.icon}</div>
                <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-2">
                  {feature.title}
                </h3>
                <p className="text-gray-600 dark:text-gray-400 text-sm">
                  {feature.desc}
                </p>
              </motion.div>
            ))}
          </div>
        </motion.div>

        {/* How it Works */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.4 }}
          className="mt-12"
        >
          <h2 className="text-3xl font-bold text-gray-900 dark:text-white mb-8 text-center">
            How It Works
          </h2>
          <div className="bg-white dark:bg-gray-800 rounded-lg p-8 shadow-lg">
            <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
              {[
                { step: 1, title: 'Input', desc: 'Paste AI text' },
                { step: 2, title: 'Process', desc: 'Paraphrase & humanize' },
                { step: 3, title: 'Enhance', desc: 'Add human touch' },
                { step: 4, title: 'Output', desc: 'Get natural text' },
              ].map((item, idx) => (
                <div key={idx} className="relative">
                  <div className="flex flex-col items-center">
                    <div className="w-12 h-12 bg-blue-500 text-white rounded-full flex items-center justify-center font-bold mb-2">
                      {item.step}
                    </div>
                    <h3 className="font-semibold text-gray-900 dark:text-white">
                      {item.title}
                    </h3>
                    <p className="text-sm text-gray-600 dark:text-gray-400 text-center mt-1">
                      {item.desc}
                    </p>
                  </div>
                  {idx < 3 && (
                    <div className="absolute top-6 -right-2 text-2xl text-gray-400">→</div>
                  )}
                </div>
              ))}
            </div>
          </div>
        </motion.div>
      </div>
    </div>
  );
}

export default Home;
