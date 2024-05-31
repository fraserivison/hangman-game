import random
from constants import print_hangman, WORD_DICTIONARY

class HangmanGame:
    def __init__(self):
        self.player_name = ""
        self.chosen_category = ""
        self.selected_word = ""
        self.guessed_letters = set()
        self.attempts = 0
        self.display_word = []

    def get_random_word(self, category):
        """
        Select a random word from a specified category.
        """
        return random.choice(WORD_DICTIONARY[category])

    def get_player_input(self):
        """
        Prompt the player to input a letter.
        """
        while True:
            guess = input("Guess a letter: ").strip().lower()
            if len(guess) != 1 or not guess.isalpha():
                print("*** Please enter a single letter ***")
            else:
                return guess

    def show_welcome_msg(self):
        print("Hi there, welcome to Hangman!")
        print("Guess wisely, every letter counts...")
        print("---------------------------------")

    def take_username_input(self):
        """
        Prompt the player to input their name and validate it.
        """
        while True:
            player_name = input("Before we begin, what is your name?: ")
            if player_name == "":
                print("*** Name cannot be empty ***")
            elif not player_name.isalpha():
                print("*** Name can only contain letters A-Z ***")
            else:
                self.player_name = player_name
                return

    def show_rules(self):
        print(f"Hi {self.player_name}, the rules are as follows:")
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

    def play_game(self):
        """
        Play a single round of Hangman.
        """
        self.chosen_category = random.choice(list(WORD_DICTIONARY.keys()))
        self.selected_word = self.get_random_word(self.chosen_category)
        print(f"The category is: {self.chosen_category}")

        self.guessed_letters = set()
        self.attempts = 0
        self.display_word = ['_'] * len(self.selected_word)

        while self.attempts < 6:
            print(" ".join(self.display_word))
            print_hangman(self.attempts)

            guess = self.get_player_input()
            self.guessed_letters.add(guess)

            if guess in self.selected_word:
                for i, letter in enumerate(self.selected_word):
                    if letter == guess:
                        self.display_word[i] = guess
                print("Correct guess :)")
            else:
                print("Incorrect guess :(")
                self.attempts += 1

            if ''.join(self.display_word) == self.selected_word:
                print("Congratulations! You guessed the word:", self.selected_word)
                break

        if self.attempts == 6:
            print("Game Over! The word was:", self.selected_word)

    def get_yes_no_input(self, prompt):
        """
        Prompt the user for a 'yes' or 'no' response, re-prompting as necessary.
        """
        while True:
            response = input(prompt).strip().lower()
            if response in ['yes', 'no']:
                return response
            else:
                print("*** Please enter 'yes' or 'no' ***")

    def start_game(self):
        """
        Handle the starting and restarting of the game.
        """
        start_game = self.get_yes_no_input("Do you want to play Hangman? (yes/no): ")
        if start_game == 'yes':
            print("Great! Let's start the game...")
            while True:
                self.play_game()
                play_again = self.get_yes_no_input("Do you want to play again? (yes/no): ")
                if play_again != 'yes':
                    print("Thank you for playing Hangman!")
                    break
        else:
            print("Thank you for playing Hangman!")
            return

    def run(self):
        self.show_welcome_msg()
        self.take_username_input()
        self.show_rules()
        self.start_game()

if __name__ == "__main__":
    game = HangmanGame()
    game.run()
