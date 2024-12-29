# from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer
# my_bot = ChatBot(name = 'PyBot', read_only= True, logic_adapters= ['chatterbot.logic.mathematicalEvaluation', 'chatterbot.logic.BestMatch'])
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a chatbot instance
my_bot = ChatBot(
    name='PyBot',
    read_only=True,
    logic_adapters=[
        'chatterbot.logic.mathematical_evaluation.MathematicalEvaluation',
        'chatterbot.logic.BestMatch'
    ]
)

# Train the chatbot (if needed)
# trainer = ListTrainer(my_bot)
# trainer.train([
#     "Hi there!",
#     "Hello!",
#     "How are you?",
#     "I'm good, thank you.",
#     "That's great to hear!",
#     "Thank you.",
#     "You're welcome."
# ])

# Example conversation loop
while True:
    user_input = input("You: ")
    response = my_bot.get_response(user_input)
    print("Bot:", response)
