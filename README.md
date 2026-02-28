# 🇸🇪 Swedish Tutor Agent

An AI-powered Swedish language tutor built with Google Gemini API. Practice Swedish through real time grammar correction and CEFR vocabulary quizzes in a clean, Gemini-inspired web interface.

> Built as a personal learning project to explore agentic AI development using Google's Gemini API and Google Antigravity IDE.

---

## Features

### Correction Mode
- Write anything in Swedish and get instant grammar and spelling corrections
- Explanations in English so you understand *why* something is wrong
- Bilingual support. Write in English and get encouraged to try in Swedish

### Quiz Mode
- Vocabulary quizzes aligned to the **CEFR language scale** (A1 → C1)
- Gemini generates random words dynamically — never repeats within a session
- Each answer includes an example sentence in Swedish with English translation below
- Live score tracking in the sidebar

### CEFR Difficulty Levels
| Level | Name | Description |
|---|---|---|
| A1 | Beginner | Basic phrases, introductions, everyday survival vocabulary |
| A2 | Elementary | Simple routine tasks, basic everyday information |
| B1 | Intermediate | Main points in work, school, and travel situations |
| B2 | Upper Intermediate | Fluent interaction, complex texts, technical discussions |
| C1 | Advanced | Demanding texts, implicit meanings, specialized vocabulary |

---

## Web Interface

Clean, Gemini-inspired dark theme built with Streamlit:
- Sidebar with mode selector, CEFR level dropdown, and live score
- Chat area with left aligned tutor messages and right aligned user bubbles
- Fixed input bar at the bottom
- Clear chat button to reset sessions

---

## Repo Structure

The codebase is modular. AI logic is decoupled from the UI:

```
swedish-tutor-agent/
├── tutor.py            ← All Gemini API logic (correction, quiz, CEFR prompts)
├── streamlit_app.py    ← Web UI (imports from tutor.py)
├── app.py              ← Terminal UI (imports from tutor.py)
├── .env.example        ← Template for setup
└── README.md           ← App documentation
```

Both `streamlit_app.py` and `app.py` share the same AI core. Changes to tutor logic only need to be made once.

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core language |
| Google Gemini API (`gemini-2.5-flash-lite`) | AI language model |
| google-genai | Official Google Gemini SDK |
| Streamlit | Web interface |
| python-dotenv | Secure API key management |
| Google Antigravity | Agentic IDE used for development |

---

## Setup & Running Locally

### 1. Clone the repository
```bash
git clone https://github.com/jasonlohyp/swedish-tutor-agent.git
cd swedish-tutor-agent
```

### 2. Set up your API key
```bash
cp .env.example .env
```
Edit `.env` and add your [Gemini API key](https://aistudio.google.com/apikey):
```
GEMINI_API_KEY=your_api_key_here
```

### 3. Install dependencies
```bash
pip install google-genai python-dotenv streamlit
```

### 4. Run the web app
```bash
python -m streamlit run streamlit_app.py
```

Or run the terminal version:
```bash
python app.py
```

---

## Roadmap

- [x] Correction mode with grammar feedback
- [x] Quiz mode with CEFR difficulty levels
- [x] Dynamic word generation via Gemini (no hardcoded word lists)
- [x] Example sentences for every quiz word
- [x] Web UI with Gemini-inspired dark theme
- [ ] Speech mode — speak Swedish, app checks pronunciation
- [ ] Deploy to Cloud Run — live public URL

