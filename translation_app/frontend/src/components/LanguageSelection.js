import React from 'react';

function LanguageSelection({ targetLang, setTargetLang }) {
  const languages = [
    { code: 'bg', name: 'Bulgarian' },
    { code: 'cs', name: 'Czech' },
    { code: 'da', name: 'Danish' },
    { code: 'de', name: 'German' },
    { code: 'en', name: 'English' },
    { code: 'es', name: 'Spanish' },
    { code: 'fi', name: 'Finnish' },
    { code: 'fr', name: 'French' },
    { code: 'hu', name: 'Hungarian' },
    { code: 'it', name: 'Italian' },
    { code: 'lv', name: 'Latvian' },
    { code: 'nl', name: 'Dutch' },
    { code: 'pl', name: 'Polish' },
    { code: 'pt', name: 'Portuguese' },
    { code: 'ro', name: 'Romanian' },
    { code: 'sl', name: 'Slovenian' },
    { code: 'sv', name: 'Swedish' },
  ];

  return (
    <div>
      <select value={targetLang} onChange={(e) => setTargetLang(e.target.value)}>
        <option value="">Select target language</option>
        {languages.map((lang) => (
          <option key={lang.code} value={lang.code}>
            {lang.name}
          </option>
        ))}
      </select>
    </div>
  );
}

export default LanguageSelection;
