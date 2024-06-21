import React, { useState } from 'react';
import './App.css';
import TextInput from './components/TextInput';
import LanguageSelection from './components/LanguageSelection';
import TranslationResult from './components/TranslationResult';

function App() {
  const [text, setText] = useState('');
  const [detectedLang, setDetectedLang] = useState('');
  const [targetLang, setTargetLang] = useState('');
  const [translatedText, setTranslatedText] = useState('');
  const [apiKey] = useState('YOUR_GOOGLE_API_KEY'); // Replace with your API key

  const handleDetectLanguage = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/detect', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text }),
      });
      const data = await response.json();
      console.log('Detection response:', data);
      setDetectedLang(data.detected_language);
    } catch (error) {
      console.error('Error detecting language:', error);
    }
  };

  const handleTranslateText = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/translate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          text,
          target_lang: targetLang,
          api_key: apiKey,
        }),
      });
      const data = await response.json();
      console.log('Translation response:',data);
      setTranslatedText(data.translated_text);
    } catch (error) {
      console.error('Error translating text:', error);
    }
  };

  return (
    <div className="App">
      <h1>Language Detection and Translation</h1>
      <TextInput text={text} setText={setText} />
      <button onClick={handleDetectLanguage}>Detect Language</button>
      {detectedLang && <p>Detected Language: {detectedLang}</p>}
      <LanguageSelection targetLang={targetLang} setTargetLang={setTargetLang} />
      <button onClick={handleTranslateText}>Translate</button>
      <TranslationResult translatedText={translatedText} />
    </div>
  );
}

export default App;
