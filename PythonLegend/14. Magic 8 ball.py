# Write code below 💖

import random

question = input("Question: ")

random_question = random.randint(1,9)

if random_question == 1:
    print("Yes, definitely.")
elif random_question == 2:
    print("It is decidedly so.")
elif random_question == 3:
    print("Without a doubt.")
elif random_question == 4:
    print("Reply hazy, try again.")
elif random_question == 5:
    print("Ask again later.")
elif random_question == 6:
    print("Better not tell you now.")
elif random_question == 7:
    print("My sources say no.")
elif random_question == 8:
    print("Outlook not so good.")
else:
    print("Very doubtful.")