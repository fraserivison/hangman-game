# Function to print the hangman based on the number of wrong guesses
# code taken from-
# (https://github.com/ShaunHalverson/PythonHangman/blob/main/main.py)
def print_hangman(wrong):
    if wrong == 0:
        print("")
        print("+---+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif wrong == 1:
        print("")
        print("+---+")
        print("O   |")
        print("    |")
        print("    |")
        print("   ===")
    elif wrong == 2:
        print("")
        print("+---+")
        print("O   |")
        print("|   |")
        print("    |")
        print("   ===")
    elif wrong == 3:
        print("")
        print("+---+")
        print(" O  |")
        print("/|  |")
        print("    |")
        print("   ===")
    elif wrong == 4:
        print("")
        print("+---+")
        print(" O  |")
        print("/|\\ |")
        print("    |")
        print("   ===")
    elif wrong == 5:
        print("")
        print("+---+")
        print(" O  |")
        print("/|\\ |")
        print("/   |")
        print("   ===")
    elif wrong == 6:
        print("")
        print("+---+")
        print(" O   |")
        print("/|\\  |")
        print("/ \\  |")
        print("    ===")


# Dictionary containing word categories
WORD_DICTIONARY = {
    "Animals": [
        "platypus", "meerkat", "kangaroo", "warthog", "lobster",
        "leopard", "goose"
    ],
    "Countries": [
        "mexico", "nepal", "greenland", "denmark", "slovenia",
        "scotland", "liechtenstein"
    ],
    "Food": [
        "banana", "pickles", "spaghetti", "cheesecake", "olives",
        "yoghurt",
    ]
}