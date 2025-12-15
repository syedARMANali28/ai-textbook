// humanoid-ai-textbook/src/components/RagChat.jsx

import React, { useState } from 'react';

const API_BASE_URL = typeof window !== 'undefined' ? (window.location.protocol + '//' + window.location.host) : 'http://localhost:8000'; // Fallback for SSR

function RagChat() {
  const [chatInput, setChatInput] = useState('');
  const [chatMessages, setChatMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleChatSubmit = async (e) => {
    e.preventDefault();
    if (!chatInput.trim()) return;

    const userMessage = { sender: 'user', text: chatInput };
    setChatMessages((prev) => [...prev, userMessage]);
    setLoading(true);

    try {
      const response = await fetch(`${API_BASE_URL}/api/v1/chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query_text: chatInput }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      const botMessage = { sender: 'bot', text: data.response_text, sources: data.sources };
      setChatMessages((prev) => [...prev, botMessage]);
    } catch (error) {
      console.error('Chat API Error:', error);
      setChatMessages((prev) => [...prev, { sender: 'bot', text: `Error: ${error.message}` }]);
    } finally {
      setChatInput('');
      setLoading(false);
    }
  };

  return (
    <div style={{ border: '1px solid #ccc', padding: '15px', borderRadius: '8px', boxShadow: '0 2px 4px rgba(0,0,0,0.1)', fontFamily: 'Arial, sans-serif', maxWidth: '600px', margin: '20px 0' }}>
      <h3>Ask the Module Chatbot</h3>
      <div style={{ height: '250px', overflowY: 'auto', border: '1px solid #eee', padding: '10px', marginBottom: '10px', borderRadius: '4px', backgroundColor: '#f9f9f9' }}>
        {chatMessages.map((msg, index) => (
          <div key={index} style={{ marginBottom: '8px', textAlign: msg.sender === 'user' ? 'right' : 'left' }}>
            <strong style={{ color: msg.sender === 'user' ? '#007bff' : '#28a745' }}>{msg.sender === 'user' ? 'You' : 'Bot'}:</strong> {msg.text}
            {msg.sources && msg.sources.length > 0 && (
              <div style={{ fontSize: '0.8em', color: '#666', marginTop: '4px' }}>
                <strong>Sources:</strong>
                {msg.sources.map((src, srcIndex) => (
                  <span key={srcIndex} style={{ display: 'block' }}>
                    - {src.module}/{src.chapter}/{src.section_title}
                  </span>
                ))}
              </div>
            )}
          </div>
        ))}
        {loading && <div style={{ color: '#888' }}>Bot is thinking...</div>}
      </div>
      <form onSubmit={handleChatSubmit} style={{ display: 'flex' }}>
        <input
          type="text"
          value={chatInput}
          onChange={(e) => setChatInput(e.target.value)}
          placeholder="Type your question here..."
          style={{ flex: 1, padding: '8px', border: '1px solid #ccc', borderRadius: '4px', marginRight: '8px' }}
          disabled={loading}
        />
        <button type="submit" style={{ padding: '8px 15px', backgroundColor: '#007bff', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer' }} disabled={loading}>
          Send
        </button>
      </form>
    </div>
  );
}

export default RagChat;
