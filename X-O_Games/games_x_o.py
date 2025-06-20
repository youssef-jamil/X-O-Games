# X-O Game
# This version of the X-O game is designed for two players and the player number two be a human not a bot or computer or machine.
# the game is played on a 3x3 grid
# the first player is X and the second player is O
# the game ends when one player has three in a row, or when the grid is full
# I have a classes for the game and the player and a function to play the game
# I have a four classes: Game, Player, Board, and Menu
import os


def clear_screen():
    # Clear the console screen for better visibility
    os.system("cls" if os.name == "nt" else "clear")


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
#            self.board = [[" " for _ in range(3)] for _ in range(3)]


class Game:
    def __init__(self):
        self.board = Board()
        self.menu = Menu()
        self.players = [Player(), Player()]
        self.current_player = 0

    def print_player_info(self, player_index):
        print(
            f"{self.players[player_index].name} will play with {self.players[player_index].symbol}."
        )

    def setup_players(self):
        print("The game will be played between two players.")
        print("For the first player: ")
        self.players[0].choose_name()
        self.players[0].choose_symbol()
        print(f"{self.players[0].name} will play with {self.players[0].symbol}.")
        clear_screen()
        print("For the second player: ")
        # The second player will automatically get the opposite symbol
        self.players[1].choose_name()
        self.players[1].symbol = "O" if self.players[0].symbol == "X" else "X"
        self.print_player_info(1)
        clear_screen()
        print("The game is ready to start!")
        self.print_player_info(0)
        self.print_player_info(1)

    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == "1":
            self.setup_players()
            self.play_game()
        elif choice == "2":
            print("Thank you for playing! Goodbye!")
            exit()

    def play_game(self):
        while True:
            clear_screen()
            self.play_turn()
            if self.check_winner() or self.check_draw():
                choice = self.menu.display_endgame_menu()
                if choice == "1":
                    self.restart_game()
                elif choice == "2":
                    print("Thank you for playing! Goodbye!")
                    break

    def play_turn(self):
        # Plays a single turn of the game.
        # Displays the current board, prompts the current player for a move,
        # updates the board, checks for a winner or draw, and switches players.
        player = self.players[self.current_player]
        self.board.display()
        print(f"{player.name}'s turn ({player.symbol}):")
        # Get the player's move
        while True:
            try:
                step_move = int(input("Choose a position (1-9): "))
                if (1 <= step_move <= 9) and self.board.update_board(
                    step_move, player.symbol
                ):
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")

        self.switch_player()

    # def play_turn(self):
    #    self.board.display()
    #    current_player = self.players[self.current_player]
    #   print(f"{current_player.name}'s turn ({current_player.symbol}):")
    #   position = input("Choose a position (1-9): ")

    #   if not position.isdigit() or not self.board.update_board(
    #           int(position), current_player.symbol
    #   ):
    #       print("Invalid move. Try again.")
    #       return False

    #   if self.check_winner(self):
    #       self.board.display()
    #       print(f"Congratulations {current_player.name}! You win!")
    #       return True

    #   if self.board.is_full():
    #       self.board.display()
    #       print("It's a draw!")
    #       return True

    #   self.current_player = 1 - self.current_player
    #   return False

    # Switches the current player to the next player.
    # This method is called after each turn to alternate between players.
    def switch_player(self):
        self.current_player = 1 - self.current_player

    # Checks if the current player has won the game.
    # It checks all possible winning conditions (rows, columns, diagonals)1
    def check_winner(self):
        win_conditions = [
            [0, 1, 2],  # row one
            [3, 4, 5],  # row two
            [6, 7, 8],  # row three
            [0, 3, 6],  # column one
            [1, 4, 7],  # column two
            [2, 5, 8],  # column three
            [0, 4, 8],  # main diagonal
            [2, 4, 6],  # anti diagonal
        ]

        for condition in win_conditions:
            a, b, c = condition
            if self.board.board[a] == self.board.board[b] == self.board.board[
                c
            ] and self.board.board[a] in ["X", "O"]:
                print(
                    f"Congratulations {self.players[self.current_player].name}! You win!"
                )
                return True
        return False

    def check_draw(self):
        if self.board.is_full():
            print("It's a draw!")
            return True
        return False

    def restart_game(self):
        self.board = Board()
        self.current_player = 0
