import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome To Guess The Number")

    while True:
        guess = int(input("Guess a number between 1 and 100"))
        attempts += 1

        if guess == secret_number:
            print(f"congratulations ! You guessed the number in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low Try again.")
        else:
            print("too high try again.")

    play_again = input("Do you want to play again? (yes/No): ")
    return play_again == "yes"

while guess_the_number():
    pass

print("Thanks for playing!")