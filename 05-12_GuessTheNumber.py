from random import randint

name = input('Hi, what is your name?\n')
print(f'Hi {name}, I am thinking of a number between 1 and 20.')
secretNumber = randint(1,20)

for guessesTaken in range(1,7):
    guess = int(input("Take a guess.\n"))
    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break # break the loop when 
if guess == secretNumber:
    print(f"Well done, {name}! My number was {secretNumber}. You took {guessesTaken} guesses.")
else:
    print(f"Nope, the number I was thinking of was {secretNumber}")
