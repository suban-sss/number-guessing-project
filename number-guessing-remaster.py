#Algorithm: Number Guessing Game - Remastered
# 1. Import the random module to generate a random number.
# 2. Generate a random number between 1 and n (where n is the upper limit of the range).
# 3. Initialize a counter for attempts and set the maximum attempts allowed.
# 4. setting the difficulty level based on user input.
# 5. Display a welcome message and instructions for the game.
# 6. using functions to handle different difficulty levels.

#improvements for the number guessing game
#1. display level of difficulty: easy, medium, hard
# Easy mode: 15 attempts, number range 1-25, 1point per correct guess
# Medium mode: 10 attempts, number range 1-50, 3 points per correct guess
# Hard mode: 5 attempts, number range 1-100, 5 points per correct guess
#2. display score at the end of the game
#3. add a replay option to play the game again

import random
import time
import threading

# Global flag to track if time is up
time_up = False

# Function to start a timer in a separate thread
def start_timer(duration):
    global time_up # Use global variable to track time status and represent time up
    time_remaining = duration #time in seconds
    while time_remaining > 0 and not time_up: #if the time is not up
        time.sleep(1) #sleep for 1 second
        time_remaining -= 1
    if time_remaining <= 0: #if the time is up
        global time_up
        time_up = True # Set the time_up flag to True
        print("\nRing Ring Ring! Your time is up!")

# Function to play the game
def play_game(difficulty): 
    global time_up

    # Set parameters based on difficulty
    if difficulty == '1':  # Easy mode
        max_range = 25
        max_attempts = 15
        points_per_correct_guess = 1
    elif difficulty == '2':  # Medium mode
        max_range = 50
        max_attempts = 10
        points_per_correct_guess = 3
    else:  # Hard mode
        max_range = 100
        max_attempts = 5
        points_per_correct_guess = 5
        time_up = False  # Reset time_up flag for each game
        print("You have 1 minute to guess the number. Good luck!")
        timer_thread = threading.Thread(target=start_timer, args=(120)) #create a timer thread for 60 seconds
        timer_thread.start() #Start the timer in a separate thread

# Generate a random number
    selected_number = random.randint(1, max_range) 
    attempts = 0

#displaying the game role
    print(f"\nI've selected a number between 1 and {max_range}. You have {max_attempts} attempts.")

    while attempts < max_attempts: # while the attempts are less than the maximum attempts
        if difficulty == '3' and time_up: # If in hard mode and time is up
            print("⏰ Time's up! You couldn't guess the number in time.") #display a message that the time is up
            break

        try:
            #displaying the number of attempts and asking for a guess
            guess = int(input(f"[Attempt {attempts + 1}/{max_attempts}] Enter your guess: ")) 
        # If the input is not a valid integer, catch the ValueError
        except ValueError:
            print("Please enter a valid number.")
            continue

# Checking if the guess is within the valid range
        attempts += 1
        if guess < selected_number:
            print("The number is higher than your guess!")
        elif guess > selected_number:
            print("The number is lower than your guess!")
        else:
            print(f"🎉 Congratulations! You guessed the number {selected_number} correctly!")
            if difficulty == '3':
                print("+30 seconds added to your time limit!")  # Just a visual reward
            return points_per_correct_guess

# If the user has used all attempts without guessing correctly
    if difficulty == '3' and not time_up:
        time_up = True  # Gracefully stop the timer

    print(f"\nYou've used {attempts} attempts. The correct number was {selected_number}.")
    return 0

total_score = 0  # This variable will keep track of the total score across multiple rounds
while True: # Main loop to allow replaying the game
    print("\nWelcome to the Number Guessing Game!")
    print("Choose the difficulty level:")
    print("1. Easy: 15 attempts / 1 point per correct guess")
    print("2. Medium: 10 attempts / 3 points per correct guess")
    print("3. Hard: 5 attempts / 5 points per correct guess + 1-minute timer")

    while True: # Loop until a valid difficulty level is entered
        # Asking the user to input the difficulty level
        difficulty = input("Enter the difficulty level (1/2/3): ")
        if difficulty in ['1', '2', '3']:
            break
        print("Invalid input. Please enter 1, 2, or 3.")

    score = play_game(difficulty) # Call the play_game function with the selected difficulty
    total_score += score # Update the total score with the score from this round
    print(f"Score this round: {score}")
    print(f"Total score: {total_score}")

    play_again = input("Would you like to play again? (yes/no): ").lower() # Ask if the user wants to play again
    if play_again != 'yes':
        print("Thanks for playing! Final score:", total_score)
        break
