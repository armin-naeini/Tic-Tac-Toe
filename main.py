# ------- Import -------
import tkinter as tk
from tkinter import messagebox
import math

# ------- Varible -------
player = 'X'
btn = [['', '', ''], ['', '', ''], ['', '', '']]
table = [['', '', ''], ['', '', ''], ['', '', '']]

# ------- Function Game -------
def start_single_player_game(root):
    # ------- Close root -------
    root.destroy()

    # ------- setting -------
    root_game = tk.Tk()
    root_game.resizable(False, False)
    root_game.title("Tic Tac Toe")

    # ------- Button -------
    for i in range(3):
        for j in range(3):
            btn[i][j] = tk.Button(root_game, font=('Verdana', 56), width=3, bg='light blue')
            btn[i][j].grid(row=i, column=j)

    # ------- Run -------
    root_game.mainloop()

def start_double_player_game(root):
    # ------- Close root -------
    root.destroy()

    # ------- setting -------
    root_game = tk.Tk()
    root_game.resizable(False, False)
    root_game.title("Tic Tac Toe")

    # ------- Button -------
    for i in range(3):
        for j in range(3):
            btn[i][j] = tk.Button(root_game, font=('Verdana', 56), width=3, bg='yellow')
            btn[i][j].grid(row=i, column=j)

    # ------- Run -------
    root_game.mainloop()

# ------- setting -------
root = tk.Tk()
root.geometry(f"{200}x{150}")
root.resizable(False, False)
root.title("Tic Tac Toe")

# ------- Frame -------
frame = tk.Frame(root).pack(pady=20)

# ------- Button -------
single_player_button = tk.Button(frame, text="Single Player", width=20, command=lambda x = root: start_single_player_game(root)).pack(pady=10)
double_player_button = tk.Button(frame, text="Double Player", width=20, command=lambda x = root: start_double_player_game(root)).pack(pady=10)

# ------- Run -------
root.mainloop()