import os
import sys
from google import genai

def main():
    # The API key should be read from an environment variable called GEMINI_API_KEY
    api_key = os.environ.get("GEMINI_API_KEY")
    
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set.")
        sys.exit(1)

    # Using the new google-genai library as recommended
    client = genai.Client(api_key=api_key)

    # System instruction for the Swedish language tutor
    system_prompt = (
        "You are a friendly Swedish language tutor. When the user writes in Swedish, "
        "correct any grammar or spelling mistakes, explain what was wrong in English, "
        "and show the corrected version. If the user writes in English, respond in English "
        "and encourage them to try saying it in Swedish."
    )

    print("--- Swedish Language Tutor ---")
    print("Type 'quit' or 'exit' to end the session.")
    print("-------------------------------")

    # The app runs as a chat loop in the terminal
    chat = client.chats.create(
        model="gemini-2.5-flash-lite",
        config={"system_instruction": system_prompt}
    )

    while True:
        try:
            user_input = input("\nYou: ").strip()
            
            if user_input.lower() in ["quit", "exit"]:
                print("Hej då! (Goodbye!)")
                break
                
            if not user_input:
                continue

            response = chat.send_message(user_input)
            print(f"\nTutor: {response.text}")

        except KeyboardInterrupt:
            print("\nHej då! (Goodbye!)")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()
