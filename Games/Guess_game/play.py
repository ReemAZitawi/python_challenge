import random

def guess_the_number():
    print("Welcome to the Guess the Number Game!")

    while True:

        lower_number = int(input("Enter the lower number of the range: "))
        upper_number = int(input("Enter the upper number of the range: "))


        target_number = random.randint(lower_number, upper_number)


        attempts = 0
        guessed_number = None

        print(f"\nGuess the number between {lower_number} and {upper_number}:")


        while guessed_number != target_number:
            guessed_number = int(input())
            attempts += 1

            if guessed_number < target_number:
                print("Too low! Try again.")
            elif guessed_number > target_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the correct number ({target_number}) in {attempts} attempts.")


        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Hope to see you again soon!")
            break

if __name__ == "__main__":
    guess_the_number()