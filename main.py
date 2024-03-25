# ------- Import -------
import tkinter as tk
from tkinter import messagebox
import math

# ------- Varible -------
player = 'X'
btn = [['', '', ''], ['', '', ''], ['', '', '']]
table = [['', '', ''], ['', '', ''], ['', '', '']]


# ------- setting -------
root = tk.Tk()
root.geometry(f"{200}x{150}")
root.resizable(False, False)
root.title("Tic Tac Toe")

# ------- Frame -------
frame = tk.Frame(root).pack(pady=20)

# ------- Button -------
single_player_button = tk.Button(frame, text="Single Player", width=20).pack(pady=10)
double_player_button = tk.Button(frame, text="Double Player", width=20).pack(pady=10)

# ------- Run -------
root.mainloop()