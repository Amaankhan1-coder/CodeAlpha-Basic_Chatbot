responses={
    "how are you": ["I'm fine,thanks!"],
    "bye": ["goodbye!"],
    "hello": ["Hi!"]
}
while True:
    user_input=input("You: ")
    if user_input.lower() in responses:
        bot_reply=(responses[user_input.lower()])
        print("Bot:",bot_reply)
    else:
        print("Bot: I am sorry")