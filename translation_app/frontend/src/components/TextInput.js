import React from 'react';

const TextInput = ({ text, setText }) => {
  const handleChange = (event) => {
    setText(event.target.value);
  };

  return (
    <div>
      <input
        type="text"
        placeholder="Enter text"
        value={text}
        onChange={handleChange}
      />
    </div>
  );
};

export default TextInput;
