### Word learing task

import os
import time

# List of words
words = ["hello", "world", "python", "code", "example"]

# Iterate over the words
# Reverse: reversed(words)
# Random: for _ in range(5):
for word in words: 
    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Print the word
    print(word) # Random: word = random.choice(words)
    
    # Wait for 3 seconds
    time.sleep(3)
    
    
### Simple reaction time task

import os
import time
import random

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# List of texts for the user to react to
texts = ["Ready?", "Set", "Go!"]

# Iterate over the texts
for text in texts:
    clear_screen()  # Clear the screen
    
    # Print the text and record the start time
    print(text)
    start_time = time.time()
    
    # Wait for the user to press Enter
    input("Press Enter to continue...")
    
    # Calculate the reaction time
    reaction_time = time.time() - start_time
    
    # Print the reaction time
    print("Reaction time:", reaction_time, "seconds")
    
    # Wait for a random amount of time before the next trial (between 1 and 5 seconds)
    wait_time = random.uniform(1, 5)
    time.sleep(wait_time)
    

### Guessing number game

import random

def play_game():
    # Generate a random number between 1 and 6
    correct_number = random.randint(1, 6)

    # Keep asking for guesses until the user makes the correct guess
    while True:
        # Ask the user to guess the number
        guess = int(input("Guess the number between 1 and 6: "))
        
        # Check if the guess is correct
        if guess == correct_number:
            print("Congratulations! You guessed the correct number:", correct_number)
            break
        else:
            # If the guess is incorrect, provide a hint
            if guess < correct_number:
                print("Incorrect guess. The correct number is larger.")
            else:
                print("Incorrect guess. The correct number is smaller.")
    
    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ")
    return play_again.lower() == 'yes'

# Main loop to play the game
while True:
    if not play_game():
        print("Thanks for playing! Goodbye.")
        break


### Guessing number game (user thinks, computer guesses)

import random

def computer_guess_number():
    # Initial range of possible numbers
    lower_bound = 1
    upper_bound = 100
    
    while True:
        # Computer makes a guess
        guessed_number = random.randint(lower_bound, upper_bound)
        
        # Ask user if the guessed number is correct, too high, or too low
        feedback = input(f"Is {guessed_number} your number? (yes/too high/too low): ").lower()
        
        # Check user's feedback
        if feedback == 'yes':
            print("Hooray! The computer guessed your number correctly.")
            break
        elif feedback == 'too high':
            upper_bound = guessed_number - 1
        elif feedback == 'too low':
            lower_bound = guessed_number + 1
        else:
            print("Invalid feedback. Please enter 'yes', 'too high', or 'too low'.")

# Play the game
computer_guess_number()
