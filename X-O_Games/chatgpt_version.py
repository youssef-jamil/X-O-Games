import tkinter as tk
from tkinter import messagebox
import random


class XOGameVsComputer:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("X-O Game vs Computer")

        self.player_symbol = "X"
        self.computer_symbol = "O"
        self.board = [""] * 9
        self.buttons = []
        self.player_wins = 0
        self.computer_wins = 0

        self.status_label = tk.Label(self.window, text="Your turn (X)", font=("Arial", 14))
        self.status_label.grid(row=0, column=0, columnspan=3, pady=10)

        self.create_board()
        self.score_label = tk.Label(self.window, text=self.get_score_text(), font=("Arial", 12))
        self.score_label.grid(row=5, column=0, columnspan=3, pady=10)

        self.window.mainloop()

    def create_board(self):
        for i in range(9):
            button = tk.Button(
                self.window,
                text="",
                font=("Arial", 24),
                width=5,
                height=2,
                command=lambda i=i: self.player_move(i),
            )
            button.grid(row=(i // 3) + 1, column=i % 3)
            self.buttons.append(button)

    def player_move(self, index):
        if self.board[index] == "":
            self.board[index] = self.player_symbol
            self.buttons[index].config(text=self.player_symbol, state="disabled")
            if self.check_winner(self.player_symbol):
                self.player_wins += 1
                self.end_game("You win!")
                return
            if self.check_draw():
                self.end_game("It's a draw!")
                return
            self.status_label.config(text="Computer's turn (O)")
            self.window.after(500, self.computer_move)

    def computer_move(self):
        available_moves = [i for i in range(9) if self.board[i] == ""]
        if available_moves:
            index = random.choice(available_moves)
            self.board[index] = self.computer_symbol
            self.buttons[index].config(text=self.computer_symbol, state="disabled")
            if self.check_winner(self.computer_symbol):
                self.computer_wins += 1
                self.end_game("Computer wins!")
                return
            if self.check_draw():
                self.end_game("It's a draw!")
                return
            self.status_label.config(text="Your turn (X)")

    def check_winner(self, symbol):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        return any(all(self.board[i] == symbol for i in condition) for condition in win_conditions)

    def check_draw(self):
        return all(cell in ["X", "O"] for cell in self.board)

    def end_game(self, result):
        messagebox.showinfo("Game Over", f"{result}")
        self.score_label.config(text=self.get_score_text())
        if messagebox.askyesno("Play Again", "Do you want to play again?"):
            self.reset_board()
        else:
            self.window.quit()

    def reset_board(self):
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="", state="normal")
        self.status_label.config(text="Your turn (X)")

    def get_score_text(self):
        return f"You: {self.player_wins}   |   Computer: {self.computer_wins}"


if __name__ == "__main__":
    XOGameVsComputer()
