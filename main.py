import os
from dotenv import load_dotenv
from chatbot import PDF_Chatbot


load_dotenv()

def main():
    print("Welcome to the AI PDF Assistant! Make yourself at home")
    bot = PDF_Chatbot("data.pdf")
    bot.ingest()
    print("Feel free to ask questions about the document...")
    print("Type 'exit' whenever you would like to quit...")
    print("-" * 40)

    while True:
        user_input = input()
        if user_input == "exit":
            print("Goodbye, it was nice chatting with you!")
            break
        if not user_input.split():
            continue
        try:
            response = bot.ask_question(user_input)
            print(f"\nAI: {response['answer']}")
        except Exception as e:
            print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()

