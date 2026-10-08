import random

secret_number=random.randint(1, 100)
attempts=0

print("=== Number Guessing Game (1-100) ===")

while True:
    guess=int(input("Guess a number (1-100): "))
    attempts+=1
    if guess<secret_number:
        print("Higher!")
    elif guess>secret_number:
        print("Lower!")
    else:
        print(f"Correct!You guessed it in {attempts} attempts!")
        break