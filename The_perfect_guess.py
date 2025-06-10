import random  # For generating random numbers

computer_no = random.randint(1, 100)  # Random number between 1 and 100
guesses = 0  # Guess counter

# print(computer_no)  # For testing

while True:
    num = int(input("Guess any number from 1 to 100: "))
    guesses += 1

    if num == computer_no:
        if guesses == 1:
            print("🎉 Correct Guess! You guessed it in 1 attempt.")
        else:
            print(f"🎉 Correct Guess! You guessed it in {guesses} attempts.")
        break
    elif num < computer_no:
        print("Higher number :)")
    else:
        print("Lower number :)")
