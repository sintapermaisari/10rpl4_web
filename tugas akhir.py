import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.turn = "X"
        self.board = [""] * 9

        self.buttons = []
        for i in range(9):
            btn = tk.Button(master, text="", font=('Arial', 24), width=5, height=2,
                            command=lambda i=i: self.click(i))
            btn.grid(row=i//3, column=i%3)
            self.buttons.append(btn)

    def click(self, index):
        if self.buttons[index]["text"] == "":
            self.buttons[index]["text"] = self.turn
            self.board[index] = self.turn
            if self.check_winner(self.turn):
                messagebox.showinfo("Game Over", f"{self.turn} Menang!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "Seri!")
                self.reset_game()
            else:
                self.turn = "O" if self.turn == "X" else "X"

    def check_winner(self, player):
        win_conditions = [
            (0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)
        ]
        for a, b, c in win_conditions:
            if self.board[a] == self.board[b] == self.board[c] == player:
                return True
        return False

    def reset_game(self):
        for btn in self.buttons:
            btn["text"] = ""
        self.board = [""] * 9
        self.turn = "X"

# Jalankan game-nya
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
