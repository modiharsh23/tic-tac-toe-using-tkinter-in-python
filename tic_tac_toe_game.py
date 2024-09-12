import tkinter as tk
from tkmacosx import Button
import random as ran

def set_tile(row,column):
    global curr_player

    if (game_over):
        return

    if board[row][column]["text"] != "":
        return

    board[row][column]["text"] = curr_player

    if curr_player == 'O' :
        curr_player = 'X'
    else:
        curr_player = 'O'

    label["text"] = curr_player+"'s Turn"

    check_win()

def check_win():
    global turns, game_over
    turns +=1

    for row in range(3):
        if(board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"]+" is Winner!!!", foreground=c_yellow)
            for column in range(3):
                board[row][column].config(foreground=c_yellow, background=c_light_gray)
            game_over = True
            return
    
    for column in range(3):
        if(board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"] and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"]+" is Winner!!!", foreground=c_yellow)
            for row in range(3):
                board[row][column].config(foreground=c_yellow, background=c_light_gray)
            game_over = True
            return
        
    if(board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and board[0][0]["text"] != ""):
            label.config(text=board[0][0]["text"]+" is Winner!!!", foreground=c_yellow)
            for i in range(3):
                board[i][i].config(foreground=c_yellow, background=c_light_gray)
            game_over = True
            return 
    
    if(board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] and board[0][2]["text"] != ""):
            label.config(text=board[0][2]["text"]+" is Winner!!!", foreground=c_yellow)
            board[0][2].config(foreground=c_yellow, background=c_light_gray)
            board[1][1].config(foreground=c_yellow, background=c_light_gray)
            board[2][0].config(foreground=c_yellow, background=c_light_gray)
            game_over = True
            return 
    
    if (turns==9):
        game_over=True
        label.config(text="It's a Tie!!!", foreground=c_yellow)


def  new_game():
    global turns, game_over

    turns = 0
    game_over = False

    label["text"] = curr_player +"'s Turn"
    label.config(foreground='white')

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", font=('Consolas', 50, "bold"), bg=c_gray, fg=c_blue)
    

players = ['X','O']
curr_player = ran.choice(players)
board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

c_blue = '#4584b6'
c_yellow = '#ffde57'
c_gray = '#343434'
c_light_gray = '#646464'

turns = 0
game_over = False

window = tk.Tk()
window.title('TIC TAC TOE')
window.resizable(False,False)

frame = tk.Frame(window)
label = tk.Label(frame, text=curr_player+"'s turn", font=('Consolas',30,'bold'), background=c_gray, foreground="white",)
label.grid(row=0,column=0,columnspan=3,sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = Button(frame, text="", font=('Consolas', 50, "bold"), bg=c_gray, fg=c_blue, width=150, height=150, command=lambda row=row, column=column: set_tile(row,column))
        board[row][column].grid(row=row+1,column=column)

label_restart = Button(frame, text="RESTART", font=('Consolas',20,'bold'), background=c_gray, foreground="white", width=200, height=100, command=new_game)
label_restart.grid(row=4,column=0,columnspan=3,sticky='we')

frame.pack()

window.update()
win_width = window.winfo_width()
win_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

win_x = int((screen_width/2) - (win_width/2))
win_y = int((screen_height/2) - (win_height/2))

window.geometry(f"{win_width}x{win_height}+{win_x}+{win_y}")

window.mainloop()