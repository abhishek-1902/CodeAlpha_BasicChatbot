def chatbot_response(user_input):
    """Return a response based on the user's message."""

    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        return "Hi! Nice to meet you."

    elif "how are you" in user_input:
        return "I'm fine, thanks! How are you?"

    elif "your name" in user_input:
        return "I'm CodeBot, a simple Python chatbot."

    elif "what can you do" in user_input:
        return "I can respond to basic greetings and simple questions."

    elif "thank" in user_input:
        return "You're welcome!"

    elif user_input in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a great day."

    else:
        return "Sorry, I don't understand that yet."


def main():
    print("=" * 45)
    print("          BASIC PYTHON CHATBOT")
    print("=" * 45)

    print("Type 'bye' to end the conversation.\n")

    while True:
        user_input = input("You: ")

        response = chatbot_response(user_input)

        print("Bot:", response)

        if user_input.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
            break


if __name__ == "__main__":
    main()