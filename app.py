import os
import sys
import random
from dotenv import load_dotenv
from google import genai

# Model to use for all AI interactions
MODEL_NAME = "gemini-2.5-flash-lite"

def start_correction_mode(client):
    """Refactored existing correction mode logic."""
    system_prompt = (
        "You are a friendly Swedish language tutor. When the user writes in Swedish, "
        "correct any grammar or spelling mistakes, explain what was wrong in English, "
        "and show the corrected version. If the user writes in English, respond in English "
        "and encourage them to try saying it in Swedish."
    )

    print("\n--- Correction Mode ---")
    print("Type 'quit' or 'exit' to return to menu.")
    print("-------------------------------")

    chat = client.chats.create(
        model=MODEL_NAME,
        config={"system_instruction": system_prompt}
    )

    while True:
        try:
            user_input = input("\nYou: ").strip()
            
            if user_input.lower() in ["quit", "exit"]:
                break
                
            if not user_input:
                continue

            response = chat.send_message(user_input)
            print(f"\nTutor: {response.text}")

        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}")

def start_quiz_mode(client):
    """Refactored Quiz Mode using a stateful chat session."""
    system_prompt = (
        "You are a Swedish vocabulary Quiz Master. Your goal is to test the user's Swedish vocabulary. "
        "Rules:\n"
        "1. Pick a random common Swedish word or phrase and ask the user to translate it to English.\n"
        "2. When the user provides a translation, tell them if they are correct or wrong. **Always provide this feedback in English.**\n"
        "3. Be lenient with minor English spelling variations or missing articles (e.g., 'flicka' -> 'girl' or 'a girl' are both correct).\n"
        "4. After the evaluation, provide an example sentence using that Swedish word/phrase.\n"
        "5. Show the example sentence in Swedish first, then its English translation below it.\n"
        "6. If they were wrong, clearly show the correct translation in English before the example sentence.\n"
        "7. Keep track of the score (correct answers vs total attempts) and show it after the feedback and example sentence in English (e.g., 'Score: 3/4').\n"
        "8. Immediately after showing the score, pick a NEW word/phrase to continue the quiz. **Only the quiz word/phrase and the example sentence should be in Swedish; everything else MUST be in English.**\n"
        "9. Use the chat history to ensure you do not repeat words you have already used in this session."
    )

    print("\n--- Quiz Mode: Vocabulary Test ---")
    print("Translate the Swedish words/phrases to English.")
    print("Type 'quit' or 'exit' to return to menu.")
    print("-----------------------------------------")

    chat = client.chats.create(
        model=MODEL_NAME,
        config={"system_instruction": system_prompt}
    )

    # Trigger the first question
    try:
        response = chat.send_message("Let's start the quiz. Give me the first word.")
        print(f"\nTutor: {response.text}")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        return

    while True:
        try:
            user_input = input("\nYou: ").strip()

            if user_input.lower() in ["quit", "exit"]:
                break
            
            if not user_input:
                continue

            response = chat.send_message(user_input)
            print(f"\nTutor: {response.text}")

        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            break

def main():
    # Load environment variables from .env file
    load_dotenv()
    
    # The API key should be read from an environment variable called GEMINI_API_KEY
    api_key = os.environ.get("GEMINI_API_KEY")
    
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set.")
        sys.exit(1)

    # Using the new google-genai library as recommended
    client = genai.Client(api_key=api_key)

    while True:
        print("\n--- Swedish Language Tutor ---")
        print("1. Correction Mode - I write Swedish and you correct me")
        print("2. Quiz Mode - Test my Swedish vocabulary")
        print("3. Exit")
        
        choice = input("\nChoose an option (1-3): ").strip()

        if choice == '1':
            start_correction_mode(client)
        elif choice == '2':
            start_quiz_mode(client)
        elif choice == '3' or choice.lower() in ["quit", "exit"]:
            print("Hej då!")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()

