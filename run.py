import random
from constants import print_hangman, WORD_DICTIONARY
from colorama import Fore, Style, init

init(autoreset=True)

def get_random_word(category):
    """
    Select a random word from the given category.
    """
    return random.choice(WORD_DICTIONARY[category])

def get_player_input():
    """
    Prompt the player to input a single letter and validate it.
    """
    while True:
        try:
            guess = input("Guess a letter: ").strip().lower()
            if len(guess) != 1 or not guess.isalpha():
                raise ValueError("*** Please enter a single letter ***")
            return guess
        except ValueError as ve:
            print(Fore.RED + str(ve))
            

def show_welcome_msg():
    """
    Display a welcome message to the player.
    """
    print(Fore.GREEN + "Hi there, welcome to Hangman!")
    print("Guess wisely, every letter counts...")
    print("---------------------------------")

def take_username_input():
    """
    Prompt the player to enter their name and validate it.
    """
    while True:
        player_name = input("Before we begin, what is your name?: ")
        if player_name == "":
            print(Fore.RED + "*** Name cannot be empty ***")
        elif not player_name.isalpha():
            print(Fore.RED + "*** Name can only contain letters A-Z ***")
        else:
            return player_name

def show_rules(username):
    """
    Display the game rules to the player.
    """
    print(f"Hi {username}, the rules are as follows:")
    print("---------------------------------")
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

def play_game():
    """
    Main game loop where the player guesses letters to find the word.
    """
    chosen_category = random.choice(list(WORD_DICTIONARY.keys()))
    selected_word = get_random_word(chosen_category)
    print(f"The category is: {chosen_category}")

    guessed_letters = set()
    attempts = 0
    display_word = ['_'] * len(selected_word)

    while attempts < 6:
        print(" ".join(display_word))
        print_hangman(attempts)

        guess = get_player_input()
        guessed_letters.add(guess)

        if guess in selected_word:
            for i, letter in enumerate(selected_word):
                if letter == guess:
                    display_word[i] = guess
            print(Fore.GREEN + "Correct guess :)")
        else:
            print(Fore.RED + "Incorrect guess :(")
            attempts += 1

        if ''.join(display_word) == selected_word:
            print(Fore.GREEN + "Congratulations! You guessed the word:", selected_word)
            break

    if attempts == 6:
        print(Fore.RED + "Game Over! The word was:", selected_word)

def get_yes_no_input(prompt):
    """
    Prompt the player for a yes/no response and validate it.
    """
    while True:
        response = input(prompt).strip().lower()
        if response in ['yes', 'no']:
            return response
        else:
            print(Fore.RED + "*** Please enter 'yes' or 'no' ***")

def start_game():
    """
    Start the game and manage replaying.
    """
    start_game = get_yes_no_input("Do you want to play Hangman? (yes/no): ")
    if start_game == 'yes':
        print("---------------------------------")
        print("Great! Let's start the game...")
        while True:
            play_game()
            play_again = get_yes_no_input("Do you want to play again? (yes/no): ")
            if play_again != 'yes':
                print("---------------------------------")
                print("Thank you for playing Hangman!")
                break
    else:
        print("Thank you for playing Hangman!")
        return

def hangman_game():
    """
    Start the game by showing a welcome message, taking the username, 
    showing the rules, and starting the game.
    """
    show_welcome_msg()
    player_name = take_username_input()
    show_rules(player_name)
    start_game()

if __name__ == "__main__":
    hangman_game()
