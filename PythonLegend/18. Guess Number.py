# Write code below 💖

guess = 0
tries = 0
max_tries = 3  

while guess != 6 and tries < max_tries:
    guess = int(input("Guess the number: "))
    tries += 1

if guess == 6:
    print("You got it!")
else:
    print("Sorry, you've run out of tries.")