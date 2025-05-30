# number-guessing-project
> About the project:
Number guessing is an easiest game considered among the users where the system selectes a random number from the given range based on the difficulty of the game and serve points until all the attempts are depleted like:
1. Easy (range: 1-25, 15 attempts, points per guess: 1)
2. Medium (range: 1-50, 10 attempts, points per guess: 3)
3. Hard (range: 1-100, 5 attempts, points per guess: 5, time given: 1 minute, time added per guess: 30 seconds)

I've managed to fulfil these criteria, ensuring that the game meets its right requirements. I hope anyone would love to try-out this game and let me know the area of improvement in my codespace!

Algorithm: Number Guessing Game - Remastered
1. Import the random, time, threading module
2. Set the time limit for the game
3. Generate a random number between 1 and n (where n is the upper limit of the range).
4. Initialize a counter for attempts and set the maximum attempts allowed.
5. setting the difficulty level based on user input.
6. Display a welcome message and instructions for the game.
7. using functions to handle different difficulty levels.

> improvements made in the game:
-  display level of difficulty: easy, medium, hard:
1. Easy mode: 15 attempts, number range 1-25, 1point per correct guess
2. Medium mode: 10 attempts, number range 1-50, 3 points per correct guess
3. Hard mode: 5 attempts, number range 1-100, 5 points per correct guess
- display score at the end of the game
- add a replay option to play the game again
