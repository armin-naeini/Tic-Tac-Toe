# ------- Import -------
import tkinter as tk
from tkinter import messagebox
import math

# ------- Varible -------
player = 'X'
btn = [['', '', ''], ['', '', ''], ['', '', '']]
table = [['', '', ''], ['', '', ''], ['', '', '']]

# ------- Function -------
def call_back_AI(r, c):
    if table[r][c] == 'X' or table[r][c] == '0':
        messagebox.showerror("Error", "This house is already full !!")
        return
    btn[r][c].configure(text='X')
    table[r][c] = 'X'
    if evaluate(table) == -1:
        messagebox.showinfo("Winner", "You win!")
        clear_window()
        return
    if evaluate(table) == 1:
        messagebox.showinfo("Winner", "AI win!")
        clear_window()
        return
    if is_full(table) == True:
        messagebox.showinfo("Winner", "It's a draw!")
        clear_window()
        return
    ai_move = find_best_move(table)
    btn[ai_move[0]][ai_move[1]].configure(text='0')
    table[ai_move[0]][ai_move[1]] = '0'
    if evaluate(table) == 1:
        messagebox.showinfo("Winner", "AI win!")
        clear_window()
        return
    if is_full(table):
        messagebox.showinfo("Winner", "It's a draw!")
        clear_window()
        return

def call_back_double_player(r, c):
    global player
    if table[r][c] == 'X' or table[r][c] == '0':
        messagebox.showerror("Error", "This house is already full !!")
        return
    if player == 'X':
        btn[r][c].configure(text= 'X')
        table[r][c] = 'X'
        player = '0'
    elif player == '0':
        btn[r][c].configure(text='0')
        table[r][c] = '0'
        player = 'X'
    if evaluate(table) == -1:
        messagebox.showinfo("Winner", "Player 1 winner")
        clear_window()
        return
    if evaluate(table) == 1:
        messagebox.showinfo("Winner", "Player 2 winner")
        clear_window()
        return
    if is_full(table) == True:
        messagebox.showinfo("Winner", "It's a draw!")
        clear_window()
        return

def clear_window():
    global table
    table = [['', '', ''], ['', '', ''], ['', '', '']]
    for i in range(3):
        for j in range(3):
            btn[i][j].configure(text='')

def evaluate(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == '0':
                return 1
            elif board[i][0] == 'X':
                return -1
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == '0':
                return 1
            elif board[0][i] == 'X':
                return -1
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == '0':
            return 1
        elif board[0][0] == 'X':
            return -1
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == '0':
            return 1
        elif board[0][2] == 'X':
            return -1
    return 0

def is_full(board):
    for row in board:
        for cell in row:
            if cell == '':
                return False
    return True

def minmax(board, depth, player):
    if evaluate(board) == 1:
        return 1
    if evaluate(board) == -1:
        return -1
    if is_full(board):
        return 0
    if player == '0':
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = '0'
                    score = minmax(board, depth + 1, 'X')
                    board[i][j] = ''
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'X'
                    score = minmax(board, depth + 1, '0')
                    board[i][j] = ''
                    best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    best_score = -math.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                board[i][j] = '0'
                score = minmax(board, 0, 'X')
                board[i][j] = ''
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

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
            btn[i][j] = tk.Button(root_game, font=('Verdana', 56), width=3, bg='#4F48EC', command=lambda r=i, c=j: call_back_AI(r, c))
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
            btn[i][j] = tk.Button(root_game, font=('Verdana', 56), width=3, bg='#FF8F18', command=lambda r=i, c=j: call_back_double_player(r, c))
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