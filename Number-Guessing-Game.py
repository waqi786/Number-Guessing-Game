import random

def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 50.")
    print("You need to guess the number within a certain number of attempts.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    
    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5
    else:
        print("Invalid input. Defaulting to 'hard' difficulty.")
        attempts = 5
    
    number_to_guess = random.randint(1, 50)
    print(f"You have {attempts} attempts to guess the number. Good luck!")

    while attempts > 0:
        try:
            guess = int(input("Make a guess: "))
            if guess < 1 or guess > 50:
                print("Please guess a number between 1 and 50.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if guess > number_to_guess:
            print("Too high.")
        elif guess < number_to_guess:
            print("Too low.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} correctly!")
            break
        
        attempts -= 1
        if attempts > 0:
            print(f"You have {attempts} attempts remaining.")
        else:
            print(f"You've run out of attempts. The number was {number_to_guess}. Better luck next time!")

def main():
    while True:
        start_game()
        play_again = input("Do you want to play again? Type 'yes' or 'no': ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
