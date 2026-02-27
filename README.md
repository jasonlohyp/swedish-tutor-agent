# Swedish Language Tutor

A simple terminal-based language tutor that helps you practice Swedish using the Gemini API.

## What it Does
- **Grammar & Spelling Correction**: When you type in Swedish, the tutor provides corrections and explains mistakes in English.
- **Support for Beginners**: If you write in English, the tutor responds in English and encourages you to try Swedish.
- **Interactive Chat Loop**: Runs directly in your terminal for quick practice sessions.

## Why I Built It
Learning a new language can be intimidating, especially when you're worried about making mistakes. This project provides a low-pressure environment to practice Swedish with instant, helpful feedback from an AI tutor.

## Tech Stack
- **Python**: Core application logic.
- **Gemini API**: Powers the AI tutor using the `gemini-2.5-flash-lite` model.
- **Google Antigravity**: Developed and refined using advanced AI agentic coding.

## How to Run

### 1. Set up your API Key
Copy the `.env.example` file to a new file named `.env` and add your Gemini API key:
```bash
cp .env.example .env
```
Then edit `.env` to include your key:
```text
GEMINI_API_KEY="your_api_key_here"
```
The app will automatically load this key using `python-dotenv`.

### 2. Install Dependencies
```bash
pip install google-genai
```

### 3. Start the App
```bash
python app.py
```

## Usage
Type your messages in the prompt. To end the session, type `quit` or `exit`.