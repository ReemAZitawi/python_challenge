import random

def choose_random_word():
    word_list = ["strawberry", "watermelon", "orange", "cucumber", "flower", "pineapple", "papaya", "apple"]
    return random.choice(word_list)

def display_clues(word):
    print("\nClues:")
    print(f"- The word has {len(word)} letters.")
    print(f"- The first letter is '{word[0]}'.")
    print(f"- The word ends with '{word[-2:]}'.")

def mystery_word_game():
    print("Welcome to Mystery Word!")

    while True:

        secret_word = choose_random_word()
        attempts_left = 3


        display_clues(secret_word)


        while attempts_left > 0:
            print(f"\nAttempts left: {attempts_left}")
            player_guess = input("Guess the word: ").lower()

            if player_guess == secret_word:
                print(f"Congratulations! You guessed the word \"{secret_word}\"! Well done!")
                break
            else:
                print("Incorrect. Try again with more clues.")
                attempts_left -= 1


        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing Mystery Word! Hope to see you again soon!")
            break

if __name__ == "__main__":
    mystery_word_game()