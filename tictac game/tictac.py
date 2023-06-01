# Python Tic Tac Toe game
# ********************************************************

from tkinter import *
import random

def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:
        buttons[row][column]['text'] = player

        if check_winner():
            label.config(text=player + " wins")
        elif check_tie():
            label.config(text="Tie!")
        else:
            player = players[1] if player == players[0] else players[0]
            label.config(text=player + " turn")

def check_winner():
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "":
            buttons[i][0].config(bg="lime green")
            buttons[i][1].config(bg="lime green")
            buttons[i][2].config(bg="lime green")
            return True

    for i in range(3):
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != "":
            buttons[0][i].config(bg="lime green")
            buttons[1][i].config(bg="lime green")
            buttons[2][i].config(bg="lime green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="lime green")
        buttons[1][1].config(bg="lime green")
        buttons[2][2].config(bg="lime green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="lime green")
        buttons[1][1].config(bg="lime green")
        buttons[2][0].config(bg="lime green")
        return True

    return False

def check_tie():
    for row in buttons:
        for button in row:
            if button['text'] == "":
                return False
    return True

def new_game():
    global player

    player = random.choice(players)
    label.config(text=player + " turn")

    for row in buttons:
        for button in row:
            button.config(text="", bg="#F0F0F0")

window = Tk()
window.title("Tic-Tac-Toe")
players = ["X", "O"]
player = random.choice(players)

buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

label = Label(text=player + " turn", font=("Arial", 24), fg="#333333")
label.pack(pady=10)

reset_button = Button(text="Restart", font=("Arial", 16), command=new_game, bg="#CCCCCC")
reset_button.pack(pady=10)

frame = Frame(window, bg="#CCCCCC")
frame.pack(pady=20)

for i in range(3):
    for j in range(3):
        buttons[i][j] = Button(frame, text="", font=("Arial", 36), width=5, height=2,
                              command=lambda row=i, col=j: next_turn(row, col), bg="#EEEEEE")
        buttons[i][j].grid(row=i, column=j, padx=5, pady=5)

window.update_idletasks()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

window.mainloop()
