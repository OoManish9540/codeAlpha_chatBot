def chatbot():
    print("Chatbot: Hello! I'm your simple chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()  

        if user_input in ["hello", "hi", "hey"]:
            print("Chatbot: Hi there! How can I help you?")
        
        elif user_input in ["how are you", "how are you doing"]:
            print("Chatbot: I'm fine, thanks! How about you?")
        
        elif user_input in ["i'm fine", "i am fine", "good", "great"]:
            print("Chatbot: Glad to hear that! 😊")
        
        elif user_input in ["what is your name", "who are you"]:
            print("Chatbot: I'm a simple rule-based chatbot created by Manish.")
        
        elif user_input in ["bye", "goodbye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a great day 👋")
            break
        
        elif user_input in ["thank you", "thanks"]:
            print("Chatbot: You're welcome! 🙂")
        
        elif user_input in ["what can you do", "help"]:
            print("Chatbot: I can respond to greetings, small talk, and say goodbye.")
        
        elif user_input in ["who made you", "who created you"]:
            print("Chatbot: I was created by a Python developer like you!")
        
        elif user_input in ["what is python", "tell me about python"]: 
            print("Chatbot: Python is a powerful, easy-to-learn programming language.")
        
        elif user_input in ["time", "what time is it"]:
            from datetime import datetime
            print("Chatbot: The current time is", datetime.now().strftime("%H:%M:%S"))
        
        elif user_input in ["date", "what is today", "today's date"]:
            from datetime import datetime
            print("Chatbot: Today's date is", datetime.now().strftime("%Y-%m-%d"))
        
        else:
            print("Chatbot: Sorry, I don't understand that. Try something else!")

# Runner
chatbot()
