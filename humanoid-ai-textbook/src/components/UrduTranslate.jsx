// humanoid-ai-textbook/src/components/UrduTranslate.jsx

import React, { useState } from 'react';

const API_BASE_URL = typeof window !== 'undefined' ? (window.location.protocol + '//' + window.location.host) : 'http://localhost:8000'; // Fallback for SSR

function UrduTranslate() {
  const [translateInput, setTranslateInput] = useState('');
  const [translatedOutput, setTranslatedOutput] = useState('');
  const [translationWarning, setTranslationWarning] = useState('');
  const [loading, setLoading] = useState(false);

  const handleTranslateSubmit = async (e) => {
    e.preventDefault();
    if (!translateInput.trim()) return;

    setLoading(true);
    setTranslatedOutput('');
    setTranslationWarning('');

    const chapterTitlePlaceholder = "Current Chapter"; // Placeholder for the actual chapter title

    try {
      const response = await fetch(`${API_BASE_URL}/api/v1/translate_chapter`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ chapter_content: translateInput, chapter_title: chapterTitlePlaceholder, target_language: 'ur' }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      setTranslatedOutput(data.translated_content);
      if (data.warning) {
        setTranslationWarning(data.message);
      }
    } catch (error) {
      console.error('Translation API Error:', error);
      setTranslationWarning(`Error: ${error.message}`);
      setTranslatedOutput('Failed to translate. Displaying original content.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ border: '1px solid #ccc', padding: '15px', borderRadius: '8px', boxShadow: '0 2px 4px rgba(0,0,0,0.1)', fontFamily: 'Arial, sans-serif', maxWidth: '600px', margin: '20px 0' }}>
      <h3>Urdu Translation Tool</h3>
      <form onSubmit={handleTranslateSubmit} style={{ display: 'flex', flexDirection: 'column', marginBottom: '10px' }}>
        <textarea
          value={translateInput}
          onChange={(e) => setTranslateInput(e.target.value)}
          placeholder="Enter English content to translate..."
          rows="8"
          style={{ width: '100%', padding: '8px', border: '1px solid #ccc', borderRadius: '4px', marginBottom: '8px' }}
          disabled={loading}
        ></textarea>
        <button type="submit" style={{ padding: '8px 15px', backgroundColor: '#28a745', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer' }} disabled={loading}>
          {loading ? 'Translating...' : 'Translate to Urdu'}
        </button>
      </form>
      {translationWarning && (
        <div style={{ color: 'orange', marginBottom: '10px', border: '1px solid orange', padding: '8px', borderRadius: '4px' }}>
          {translationWarning}
        </div>
      )}
      <h4>Translated Content (Simulated):</h4>
      <div style={{ border: '1px solid #eee', padding: '10px', minHeight: '150px', backgroundColor: '#f9f9f9', borderRadius: '4px', whiteSpace: 'pre-wrap' }}>
        {translatedOutput || 'Translation will appear here.'}
      </div>
    </div>
  );
}

export default UrduTranslate;
