import openai
import os
import random
from dotenv import load_dotenv

# ✅ Load API key securely from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if api_key is None:
    raise ValueError("⚠️ OpenAI API Key not found! Make sure you have an .env file.")

# Entertainment Responses
JOKES = [
    "Why don’t skeletons fight each other? Because they don’t have the guts!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "I told my wife she should embrace her mistakes. She gave me a hug."
]

FUN_FACTS = [
    "Did you know? Honey never spoils! Archaeologists found pots of honey in ancient Egyptian tombs that are still good!",
    "Did you know? A group of flamingos is called a 'flamboyance'!",
    "Did you know? The Eiffel Tower can grow taller on hot days due to metal expansion."
]

TRIVIA_QUESTIONS = [
    "What is the name of the world's largest ocean? (Answer: Pacific Ocean)",
    "Which planet is known as the Red Planet? (Answer: Mars)",
    "Who painted the Mona Lisa? (Answer: Leonardo da Vinci)"
]

# Function to interact with OpenAI API
def chat_with_gpt(user_input):
    client = openai.OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    return response.choices[0].message.content

# Main chatbot function
def entertainment_chatbot():
    print("🎭 Welcome to the Entertainment Chatbot! Type 'exit' to stop. 🎭")
    while True:
        user_input = input("\nYou: ")

        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Have a fun day! 🎉")
            break
        elif "joke" in user_input.lower():
            print("Chatbot: " + random.choice(JOKES))
        elif "fact" in user_input.lower():
            print("Chatbot: " + random.choice(FUN_FACTS))
        elif "trivia" in user_input.lower():
            print("Chatbot: " + random.choice(TRIVIA_QUESTIONS))
        else:
            response = chat_with_gpt(user_input)
            print("Chatbot:", response)

# Run chatbot
if __name__ == "__main__":
    entertainment_chatbot()
