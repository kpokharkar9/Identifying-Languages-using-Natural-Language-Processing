import React from 'react';

function TranslationResult({ translatedText }) {
  return (
    <div>
      <textarea
        value={translatedText}
        readOnly
        placeholder="Translated text will appear here"
      />
    </div>
  );
}

export default TranslationResult;
