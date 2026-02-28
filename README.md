# Swedish Language Tutor

A powerful terminal-based language tutor that helps you practice Swedish using the Gemini API. Whether you want to practice your writing or test your vocabulary, this tutor provides instant, intelligent feedback.

## What it Does
The app features two distinct practice modes to help you master Swedish:

### 1. Correction Mode
* **Grammar & Spelling Correction**: Write freely in Swedish. The tutor will correct your mistakes and explain them in English.
* **Bilingual Support**: If you write in English, the tutor will encourage you to try Swedish while providing helpful guidance.

### 2. Quiz Mode
* **Vocabulary Testing**: Test your knowledge of Swedish words and phrases.
* **CEFR Difficulty Levels**: Choose the level that matches your skill:
  * **A1 (Beginner)**: Basic phrases, introductions, and everyday survival vocabulary.
  * **A2 (Elementary)**: Simple routine tasks and basic everyday information.
  * **B1 (Intermediate)**: Main points in work, school, and travel situations.
  * **B2 (Upper Intermediate)**: Fluent interaction and more complex technical discussions.
  * **C1 (Advanced)**: Demanding texts, implicit meanings, and specialized vocabulary.
* **Smart Feedback**: Gemini evaluates your translations (lenient with minor spelling) and provides correct answers when needed.
* **Contextual Learning**: Get an example sentence in Swedish for every word you quiz on.
* **Score Tracking**: Keep track of your accuracy throughout the session.

## Tech Stack
* **Python**: Core logic.
* **Gemini API**: Powers all AI interactions using the `gemini-2.5-flash-lite` model.
* **google-genai**: Official Google Gemini SDK.
* **python-dotenv**: For secure management of API keys.

## Setup & Running Locally

### 1. Clone the repository
```bash
git clone <repository-url>
cd swedish-tutor-agent
```

### 2. Set up your API Key
Copy the `.env.example` file to a new file named `.env`:
```bash
cp .env.example .env
```
Then edit `.env` and add your [Gemini API Key](https://aistudio.google.com/app/apikey):
```text
GEMINI_API_KEY="your_api_key_here"
```

### 3. Install Dependencies
```bash
pip install google-genai python-dotenv streamlit
```

### 4. Start the App
```bash
python -m streamlit run streamlit_app.py
```

## What's Coming Next
* **Web UI**: A beautiful, modern interface for a better practice experience.
* **Speech Mode**: Practice your pronunciation with voice-to-text and text-to-speech integration.
* **Progress Tracking**: Persistent history of your quiz scores and learning journey.

---
*Developed with advanced agentic coding for modern language learners.*
