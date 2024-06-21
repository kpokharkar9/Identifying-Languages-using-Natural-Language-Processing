# Identifying Languages and Translating Texts using Natural Language Processing

This project is a language detection and translation application. It uses a Naive Bayes model for language detection and MarianMT models along with Google Translate API for translation.

## Features

- Detect the language of input text
- Translate text from one language to another
- Supports 17 languages

## Project Structure

translation_app/
├── backend/
│ ├── app/
│ │ ├── init.py
│ │ ├── routes.py
│ │ ├── translation.py
│ ├── models/
│ │ ├── detection_model/
│ │ │ ├── mnb_model_compressed.joblib
│ │ ├── translation_model/
│ │ │ ├── {lang_pair}/
│ │ │ │ ├── model.joblib
│ │ │ │ ├── tokenizer.joblib
│ ├── run.py
│ ├── tests/
│ │ ├── conftest.py
│ │ ├── test_routes.py
├── frontend/
│ ├── public/
│ ├── src/
│ │ ├── components/
│ │ │ ├── TextInput.js
│ │ │ ├── LanguageSelection.js
│ │ │ ├── TranslationResult.js
│ │ ├── App.js
│ ├── package.json
├── venv/
├── .gitignore
├── requirements.txt
└── README.md


## Setup

### Prerequisites

- Python 3.8+
- Node.js 14+
- npm 6+

### Backend Setup

1. **Clone the repository**:

    ```sh
    git clone https://github.com/yourusername/Identifying-Languages-using-Natural-Language-Processing.git
    cd Identifying-Languages-using-Natural-Language-Processing/translation_app/backend
    ```

2. **Create a virtual environment**:

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Run the backend**:

    ```sh
    python run.py
    ```

### Frontend Setup

1. **Navigate to the frontend directory**:

    ```sh
    cd ../frontend
    ```

2. **Install the dependencies**:

    ```sh
    npm install
    ```

3. **Run the frontend**:

    ```sh
    npm start
    ```

### Running Tests

1. **Backend Tests**:

    ```sh
    cd backend
    pytest
    ```

2. **Frontend Tests**:

    ```sh
    cd ../frontend
    npm test
    ```

## Usage

1. **Open the frontend**:

    The frontend should open automatically in your default browser at `http://localhost:3000`.

2. **Enter text**:

    Enter the text you want to detect the language for or translate.

3. **Detect Language**:

    Click the "Detect Language" button to detect the language of the entered text.

4. **Translate Text**:

    Select the target language from the dropdown and click the "Translate" button to translate the text to the selected language.

## Supported Languages

- English
- Bulgarian
- Czech
- Danish
- German
- Spanish
- Finnish
- French
- Hungarian
- Italian
- Latvian
- Dutch
- Polish
- Portuguese
- Romanian
- Slovenian
- Swedish
