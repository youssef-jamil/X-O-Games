import tkinter as tk
from tkinter import messagebox
from game_x_o import Game


class GameGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("X-O Game - Player Setup")
        self.game = Game()

        self.name1_entry = tk.Entry(self.window, font=("Arial", 14))
        self.name2_entry = tk.Entry(self.window, font=("Arial", 14))
        self.symbol_var = tk.StringVar(value="X")

        self.setup_screen()

    def setup_screen(self):
        tk.Label(self.window, text="Player 1 Name:", font=("Arial", 14)).grid(
            row=0, column=0, padx=10, pady=10
        )
        self.name1_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.window, text="Choose Player 1 Symbol:", font=("Arial", 14)).grid(
            row=1, column=0, padx=10, pady=10
        )
        tk.Radiobutton(
            self.window,
            text="X",
            variable=self.symbol_var,
            value="X",
            font=("Arial", 12),
        ).grid(row=1, column=1, sticky="w")
        tk.Radiobutton(
            self.window,
            text="O",
            variable=self.symbol_var,
            value="O",
            font=("Arial", 12),
        ).grid(row=1, column=1, sticky="e")

        tk.Label(self.window, text="Player 2 Name:", font=("Arial", 14)).grid(
            row=2, column=0, padx=10, pady=10
        )
        self.name2_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Button(
            self.window, text="Start Game", font=("Arial", 14), command=self.start_game
        ).grid(row=3, column=0, columnspan=2, pady=20)

        self.window.mainloop()

    def start_game(self):
        name1 = self.name1_entry.get().strip()
        name2 = self.name2_entry.get().strip()
        symbol1 = self.symbol_var.get()
        symbol2 = "O" if symbol1 == "X" else "X"

        if not name1 or not name2:
            messagebox.showerror("Error", "Please enter both player names.")
            return

        self.game.players[0].name = name1
        self.game.players[0].symbol = symbol1
        self.game.players[1].name = name2
        self.game.players[1].symbol = symbol2

        self.window.destroy()  # Close the setup window
        self.launch_game_window()

    def launch_game_window(self):
        game_window = tk.Tk()
        game_window.title("X-O Game by Youssef Jamil")
        buttons = []
        status_label = tk.Label(game_window, text="", font=("Arial", 16))
        status_label.grid(row=0, column=0, columnspan=3, pady=10)

        def update_status():
            player = self.game.players[self.game.current_player]
            status_label.config(text=f"{player.name}'s turn ({player.symbol})")

        def update_board():
            for i in range(9):
                buttons[i].config(text=self.game.board.board[i])

        def end_game(result_text):
            choice = messagebox.askquestion("Game Over", f"{result_text}\nPlay Again?")
            if choice == "yes":
                self.game.board.reset_board()
                self.game.current_player = 0
                update_board()
                update_status()
            else:
                game_window.destroy()

        def make_move(index):
            current_player = self.game.players[self.game.current_player]
            if self.game.board.board[index] not in ["X", "O"]:
                self.game.board.board[index] = current_player.symbol
                update_board()

                if self.game.check_winner():
                    end_game(f"{current_player.name} wins!")
                elif self.game.check_draw():
                    end_game("It's a draw!")
                else:
                    self.game.switch_player()
                    update_status()

        for i in range(9):
            btn = tk.Button(
                game_window,
                text="",
                font=("Arial", 24),
                width=5,
                height=2,
                command=lambda i=i: make_move(i),
            )
            btn.grid(row=(i // 3) + 1, column=i % 3)
            buttons.append(btn)

        update_board()
        update_status()
        game_window.mainloop()


# Start the GUI application
if __name__ == "__main__":
    GameGUI()
