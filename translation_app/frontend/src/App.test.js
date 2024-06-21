import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import '@testing-library/jest-dom';
import App from './App';

global.fetch = jest.fn();

beforeEach(() => {
  fetch.mockClear();
});

test('renders Language Detection and Translation title', () => {
  render(<App />);
  const titleElement = screen.getByText(/language detection and translation/i);
  expect(titleElement).toBeInTheDocument();
});

test('detect language and translate text flow', async () => {
  // Mock the API responses
  fetch
    .mockImplementationOnce(() =>
      Promise.resolve({
        json: () => Promise.resolve({ detected_language: 'en' }),
      })
    )
    .mockImplementationOnce(() =>
      Promise.resolve({
        json: () => Promise.resolve({ translated_text: 'Hola' }),
      })
    );

  render(<App />);

  const inputElement = screen.getByPlaceholderText(/enter text/i);
  fireEvent.change(inputElement, { target: { value: 'Hello' } });

  const detectButton = screen.getByText(/detect language/i);
  fireEvent.click(detectButton);

  await waitFor(() => {
    const detectedLanguage = screen.getByText(/detected language: en/i);
    expect(detectedLanguage).toBeInTheDocument();
  });

  const selectElement = screen.getByRole('combobox');
  fireEvent.change(selectElement, { target: { value: 'es' } });

  const translateButton = screen.getByText(/translate/i);
  fireEvent.click(translateButton);

  await waitFor(() => {
    const translatedText = screen.getByDisplayValue('Hola');
    expect(translatedText).toBeInTheDocument();
  });
});
