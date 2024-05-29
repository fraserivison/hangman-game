import random

# Dictionary containing word categories
wordDictionary = {
    "Animals": ["platypus", "meerkat", "kangaroo", "warthog", "lobster", "leopard", "goose"],
    "Countries": ["mexico", "nepal", "greenland", "denmark", "slovenia", "scotland", "liechtenstein"],
    "Food": ["banana", "pickles", "spaghetti", "cheesecake", "olives", "yoghurt", ]
}

# Function to select a random word from a specified category
def get_random_word(category):
    """
    Select a random word from specified category
    """
    return random.choice(wordDictionary[category])

# Function to print the hangman based on the number of wrong guesses
def print_hangman(wrong):
  if(wrong == 0):
    print("\n+---+")
    print("    |")
    print("    |")
    print("    |")
    print("   ===")
  elif(wrong == 1): 
    print("\n+---+")
    print("O   |")
    print("    |")
    print("    |")
    print("   ===")
  elif(wrong == 2):
    print("\n+---+")
    print("O   |")
    print("|   |")
    print("    |")
    print("   ===")
  elif(wrong == 3):
    print("\n+---+")
    print(" O  |")
    print("/|  |")
    print("    |")
    print("   ===")
  elif(wrong == 4):
    print("\n+---+")
    print(" O  |")
    print("/|\ |")
    print("    |")
    print("   ===")
  elif(wrong == 5):
    print("\n+---+")
    print(" O  |")
    print("/|\ |")
    print("/   |")
    print("   ===")
  elif(wrong == 6):
    print("\n+---+")
    print(" O   |")
    print("/|\  |")
    print("/ \  |")
    print("    ===")
    # Implementation of print_hangman function...
    pass

# Function to prompt the player to input a letter
def get_player_input():
    """
    Prompt the player to input a letter.
    """
    while True:
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
        else:
            return guess

# Function to start the hangman game
def hangman_game():
    print("Hi there, welcome to Hangman!")
    print("Guess wisely, every letter counts...")
    print("---------------------------------")
    player_name = input("Before we begin, what is your name?: ")
    print(f"Hi {player_name}, the rules are as follows:")
    print("""
    1. The computer picks a word.
    2. You see blank spaces for each letter in the word.
    3. Guess letters one at a time.
    4. If the letter is in the word, the blanks are filled in.
    5. If the letter is not in the word, a part of the hangman is drawn.
    6. Keep guessing until you guess the word or the drawing is complete.
    7. You win if you guess the word before the drawing is complete.
    8. You lose if the drawing is completed before you guess the word.
    """)
    print("---------------------------------")
    
    while True:
        start_game = input("Do you want to play Hangman? (yes/no): ").strip().lower()
        if start_game == 'yes':
            print("Great! Let's start the game...")

            # Select a random word and display underscores for each letter
            selected_word = get_random_word(random.choice(list(wordDictionary.keys())))
            for _ in selected_word:
                print("_", end=" ")

            # Display initial hangman
            print_hangman(0)

            # Call function to allow player to input a letter
            get_player_input()

            # Add code for the main game logic here

            break  # Exit the loop to continue with the game
        elif start_game == 'no':
            print("Alright, let's start over.")
            print("---------------------------------")
            return hangman_game()  # Restart the function to begin again
        else:
            print("Please enter 'yes' or 'no'.") 

# Call the hangman_game function to start the process
hangman_game()

