import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Model to use for all AI interactions
MODEL_NAME = "gemini-2.5-flash-lite"

# CEFR Levels and descriptions
CEFR_LEVELS = {
    "1": ("A1 (Beginner)", "Basic phrases, introductions, and everyday survival vocabulary."),
    "2": ("A2 (Elementary)", "Simple routine tasks and basic everyday information."),
    "3": ("B1 (Intermediate)", "Main points in work/school/leisure and travel situations."),
    "4": ("B2 (Upper Intermediate)", "Fluent interaction, complex texts, and technical discussions."),
    "5": ("C1 (Advanced)", "Demanding texts, implicit meanings, and specialized vocabulary.")
}

def get_client():
    """Initializes and returns the Gemini client."""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable not set.")
    return genai.Client(api_key=api_key)

def create_correction_chat(client):
    """Creates a stateful chat session for Correction Mode."""
    system_prompt = (
        "You are a friendly Swedish language tutor. When the user writes in Swedish, "
        "correct any grammar or spelling mistakes, explain what was wrong in English, "
        "and show the corrected version. If the user writes in English, respond in English "
        "and encourage them to try saying it in Swedish."
    )
    return client.chats.create(
        model=MODEL_NAME,
        config={"system_instruction": system_prompt}
    )

def create_quiz_chat(client, level_key):
    """Creates a stateful chat session for Quiz Mode based on CEFR level."""
    level_name, level_desc = CEFR_LEVELS.get(level_key, CEFR_LEVELS["1"])
    
    system_prompt = (
        f"You are a Swedish vocabulary Quiz Master. Your goal is to test the user's Swedish vocabulary at the {level_name} level.\n"
        f"Level Description: {level_desc}\n\n"
        "Rules:\n"
        f"1. Pick a random common Swedish word or phrase appropriate for the {level_name} level and ask the user to translate it to English.\n"
        "2. When the user provides a translation, tell them if they are correct or wrong. **Always provide this feedback in English.**\n"
        "3. Be lenient with minor English spelling variations or missing articles (e.g., 'flicka' -> 'girl' or 'a girl' are both correct).\n"
        "4. After the evaluation, provide an example sentence using that Swedish word/phrase.\n"
        "5. Show the example sentence in Swedish first, then its English translation below it.\n"
        "6. If they were wrong, clearly show the correct translation in English before the example sentence.\n"
        "7. Keep track of the score (correct answers vs total attempts) and show it after the feedback and example sentence in English (e.g., 'Score: 3/4').\n"
        "8. Immediately after showing the score, pick a NEW word/phrase at the same {level_name} level to continue the quiz. **Only the quiz word/phrase and the example sentence should be in Swedish; everything else MUST be in English.**\n"
        "9. Use the chat history to ensure you do not repeat words you have already used in this session."
    )
    
    chat = client.chats.create(
        model=MODEL_NAME,
        config={"system_instruction": system_prompt}
    )
    
    # Get the first question
    response = chat.send_message(f"Let's start the {level_name} level quiz. Give me the first word.")
    return chat, response.text, level_name, level_desc

def send_message(chat, user_input):
    """Sends a message to an existing chat session and returns the response text."""
    response = chat.send_message(user_input)
    return response.text
