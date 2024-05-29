import random

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
            # Add code to start the Hangman game here
            break  # Exit the loop to continue with the game
        elif start_game == 'no':
            print("Alright, let's start over.")
            print("---------------------------------")
            return hangman_game()  # Restart the function to begin again
        else:
            print("Please enter 'yes' or 'no'.")
# Call the hangman_game function to start the process
hangman_game()

wordDictionary = {
    "Animals": ["platypus", "meerkat", "kangaroo", "warthog", "lobster", "leopard", "goose"],
    "Countries": ["mexico", "nepal", "greenland", "denmark", "slovenia", "scotland", "liechtenstein"],
    "Food": ["banana", "pickles", "spaghetti", "cheesecake", "olives", "yoghurt", ]
}

def get_random_word(category):
    """
    Select a random word from specified category
    """
    return random.choice(word_dict[category])

for x in get_random_word:
    print("_", end=" ")


