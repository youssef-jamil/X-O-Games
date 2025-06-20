import tkinter as tk
from tkinter import messagebox
from youVsComputer_version import Game
import random


class GameGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("X-O Game - Player Setup")
        self.game = Game()

        # عدد مرات الفوز
        self.player_wins = 0
        self.computer_wins = 0

        self.name1_entry = tk.Entry(self.window, font=("Arial", 14), justify="center")
        self.symbol_var = tk.StringVar(value="X")

        self.setup_screen()

    def setup_screen(self):
        tk.Label(self.window, text="Your Name:", font=("Arial", 14)).grid(
            row=0, column=0, padx=10, pady=10
        )
        self.name1_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.window, text="Choose Your Symbol:", font=("Arial", 14)).grid(
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

        tk.Button(
            self.window, text="Start Game", font=("Arial", 14), command=self.start_game
        ).grid(row=2, column=0, columnspan=2, pady=20)

        self.window.mainloop()

    def start_game(self):
        name1 = self.name1_entry.get().strip()
        symbol1 = self.symbol_var.get()
        symbol2 = "O" if symbol1 == "X" else "X"

        if not name1:
            messagebox.showerror("Error", "Please enter your name.")
            return

        self.game.players[0].name = name1
        self.game.players[0].symbol = symbol1
        self.game.players[1].name = "Computer"
        self.game.players[1].symbol = symbol2

        self.window.destroy()
        self.launch_game_window()

    def launch_game_window(self):
        game_window = tk.Tk()
        game_window.title("X-O Game by Youssef Jamil")
        buttons = []

        status_label = tk.Label(game_window, text="", font=("Arial", 16))
        status_label.grid(row=0, column=0, columnspan=3, pady=10)

        score_label = tk.Label(
            game_window, text=self.get_score_text(), font=("Arial", 12), fg="blue"
        )
        score_label.grid(row=1, column=0, columnspan=3)

        def update_status():
            player = self.game.players[self.game.current_player]
            status_label.config(text=f"{player.name}'s turn ({player.symbol})")

        def update_board():
            for i in range(9):
                buttons[i].config(text=self.game.board.board[i])

        def get_empty_positions():
            return [
                i
                for i, val in enumerate(self.game.board.board)
                if val not in ["X", "O"]
            ]

        def make_computer_move():
            empty = get_empty_positions()
            if empty:
                move = random.choice(empty)
                self.game.board.board[move] = self.game.players[1].symbol
                update_board()

                if self.game.check_winner():
                    self.computer_wins += 1
                    end_game("Computer wins!")
                elif self.game.check_draw():
                    end_game("It's a draw!")
                else:
                    self.game.switch_player()
                    update_status()

        def end_game(result_text):
            score_label.config(text=self.get_score_text())
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
                    self.player_wins += 1
                    end_game(f"{current_player.name} wins!")
                elif self.game.check_draw():
                    end_game("It's a draw!")
                else:
                    self.game.switch_player()
                    update_status()
                    make_computer_move()

        for i in range(9):
            btn = tk.Button(
                game_window,
                text="",
                font=("Arial", 24),
                width=5,
                height=2,
                command=lambda i=i: make_move(i),
            )
            btn.grid(row=(i // 3) + 2, column=i % 3)
            buttons.append(btn)

        update_board()
        update_status()
        game_window.mainloop()

    def get_score_text(self):
        return f"Wins - {self.game.players[0].name}: {self.player_wins} | Computer: {self.computer_wins}"


if __name__ == "__main__":
    GameGUI()
