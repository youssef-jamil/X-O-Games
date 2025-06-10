# X-O Game
# the game is played on a 3x3 grid
# the first player is X and the second player is O
# the game ends when one player has three in a row, or when the grid is full
# I have a classes for the game and the player and a function to play the game
# I have a four classes: Game, Player, Board, and Menu
class Player:
    def __init__(self):
        self.name = " "
        self.symbol = " "

    def choose_name(self):
        name = input("Enter your name(letters only): ")
        # Check if the name contains only letters
        while not name.isalpha():
            print("Invalid name. Please enter letters only.")
            name = input("Enter your name(letters only): ")
        self.name = name

    def choose_symbol(self):
        symbol = input("Choose your symbol (X or O): ").upper()
        # Check if the symbol is valid
        while symbol not in ["X", "O"]:
            print("Invalid symbol. Please choose X or O.")
            symbol = input("Choose your symbol (X or O): ").upper()
        self.symbol = symbol


class Menu:
    def get_valid_choice(self, prompt, valid_choices):
        choice = input(prompt)
        while choice not in valid_choices:
            print(f"Invalid choice. Please choose {', '.join(valid_choices)}.")
            choice = input(prompt)
        return choice

    def display_menu_options(self, header, options):
        print(header)
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")

    def display_main_menu(self):
        self.display_menu_options("Welcome to the X-O Game!", ["Start Game", "Exit"])
        return self.get_valid_choice("Choose an option (1 or 2): ", ["1", "2"])

    def display_endgame_menu(self):
        self.display_menu_options("Game Over!", ["Play Again", "Exit"])
        return self.get_valid_choice("Choose an option (1 or 2): ", ["1", "2"])


Menu = Menu()
Menu.display_main_menu()
