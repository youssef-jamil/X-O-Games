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


class Board:
    # ! Initializes the game board for Tic Tac Toe.
    # ! Sets up a 3x3 board represented as a list of strings numbered 1 through 9
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]

    def display(self):
        print("current board: \n")
        for i in range(3):
            print(" | ".join(self.board[i * 3 : (i + 1) * 3]))
            if i < 2:
                print("-" * 10)

    def update_board(self, position, symbol):
        # Updates the board at the specified position with the given symbol.
        # Check if the position is valid and not already occupied
        if position < 1 or position > 9:
            print("Invalid position. Please choose a number between 1 and 9.")
            return False
        if self.board[position - 1] not in ["X", "O"]:
            self.board[position - 1] = symbol
            return True
        return False

    def is_full(self):
        return all(cell in ["X", "O"] for cell in self.board)

    def reset_board(self):
        # Resets the board to its initial state.
        for i in range(9):
            self.board[i] = str(i + 1)


# ? this comment to implementation to work with row and column instead of position
# ? if you want to use this implementation, uncomment the code below
# ? if someone want to use the program with row and column instead of position
#     def __init__(self):
#         self.board = [[" " for _ in range(3)] for _ in range(3)]
#
#     def display(self):
#         for row in self.board:
#             print("|".join(row))
#             print("-" * 5)
#
#     def update(self, row, col, symbol):
#         if self.board[row][col] == " ":
#             self.board[row][col] = symbol
#             return True
#         return False
#
#     def is_full(self):
#         return all(cell != " " for row in self.board for cell in row)

#       def reset(self):
#            self.board = [[" " for _ in range(3)] for _ in range(3)] """
