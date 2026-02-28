import sys
import tutor

def start_correction_mode(client):
    """Terminal UI for Correction Mode."""
    print("\n--- Correction Mode ---")
    print("Type 'quit' or 'exit' to return to menu.")
    print("-------------------------------")

    chat = tutor.create_correction_chat(client)

    while True:
        try:
            user_input = input("\nYou: ").strip()
            
            if user_input.lower() in ["quit", "exit"]:
                break
                
            if not user_input:
                continue

            response_text = tutor.send_message(chat, user_input)
            print(f"\nTutor: {response_text}")

        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}")

def start_quiz_mode(client):
    """Terminal UI for Quiz Mode."""
    print("\nSelect CEFR Level:")
    for key, (name, desc) in tutor.CEFR_LEVELS.items():
        print(f"{key}. {name} — {desc}")
    
    diff_choice = input("\nChoose a level (1-5): ").strip()
    
    if diff_choice not in tutor.CEFR_LEVELS:
        print("Invalid choice, defaulting to A1.")
        diff_choice = "1"
        
    try:
        chat, initial_question, level_name, level_desc = tutor.create_quiz_chat(client, diff_choice)
        
        print(f"\n--- Quiz Mode: Vocabulary Test ({level_name}) ---")
        print(f"Goal: {level_desc}")
        print("Translate the Swedish words/phrases to English.")
        print("Type 'quit' or 'exit' to return to menu.")
        print("-------------------------------------------------")
        
        print(f"\nTutor: {initial_question}")

        while True:
            try:
                user_input = input("\nYou: ").strip()

                if user_input.lower() in ["quit", "exit"]:
                    break
                
                if not user_input:
                    continue

                response_text = tutor.send_message(chat, user_input)
                print(f"\nTutor: {response_text}")

            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"\nAn error occurred: {e}")
                break
    except Exception as e:
        print(f"\nFailed to start quiz: {e}")

def main():
    try:
        client = tutor.get_client()
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

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
