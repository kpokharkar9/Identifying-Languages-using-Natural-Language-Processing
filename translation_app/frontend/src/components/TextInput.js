import React from 'react';

function TextInput({ text, setText }) {
  return (
    <div>
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Enter text to detect and translate"
      />
    </div>
  );
}

export default TextInput;
