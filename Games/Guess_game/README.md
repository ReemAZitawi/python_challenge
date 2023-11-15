Task: Guess the Number Game

Create a "Guess the Number" game where the computer generates a random number between a specified range, and the player has to guess the correct number. Provide feedback to the player after each guess, indicating whether the guess was too high, too low, or correct. Also, keep track of the number of attempts.

Requirements:

The program should ask the player to input the range of numbers for the game (e.g., between 1 and 100).

The computer should generate a random number within the specified range.

The player should be prompted to guess the number.

If the guessed number is incorrect, provide feedback to the player (e.g., "Too high" or "Too low") and allow them to guess again.

Continue the game until the player guesses the correct number.

Display the number of attempts it took for the player to guess correctly.

After the game ends, ask the player if they want to play again. If yes, generate a new random number and start a new game.

Hints:

Use the random module to generate a random number.
Utilize a while loop to repeatedly prompt the player for guesses until the correct number is guessed.
Implement conditional statements (if, elif, else) to provide feedback based on the comparison between the guessed number and the random number.
Example Output:


How the user should play.

Welcome to the Guess the Number Game!

Enter the lower bound of the range: 1
Enter the upper bound of the range: 100

Guess the number between 1 and 100: 50
Too high! Try again.

Guess the number between 1 and 100: 25
Too low! Try again.

Guess the number between 1 and 100: 37
Congratulations! You guessed the correct number (37) in 3 attempts.

Do you want to play again? (yes/no): yes

Enter the lower bound of the range: 1
Enter the upper bound of the range: 50

Guess the number between 1 and 50: 25
Too high! Try again.

Guess the number between 1 and 50: 12
Too low! Try again.

Guess the number between 1 and 50: 19
Congratulations! You guessed the correct number (19) in 3 attempts.

Do you want to play again? (yes/no): no

Thanks for playing! Goodbye.







