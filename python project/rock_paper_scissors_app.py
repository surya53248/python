import tkinter as tk
import random
game=['rock','paper','scissors']
my_score=0
computer_score=0
root=tk.Tk()
root.geometry('800x800')
icon=tk.PhotoImage(file='game icon.png')
def play(my_choice):
    global my_score,computer_score
    computer_choice=random.choice(game)
    if my_choice==computer_choice:
        result_text="it's a draw!Both picked "+computer_choice
    elif my_choice=='rock' and computer_choice=='paper':
        result_text='you lose!'+"computer picked "+computer_choice
        computer_score+=1
    elif my_choice=='paper' and computer_choice=='scissors':
        result_text='you lose!'+"computer picked "+computer_choice
        computer_score+=1
    elif my_choice=='scissors' and computer_choice=='rock':
        result_text='you lose!'+"computer picked "+computer_choice
        computer_score+=1
    else:
        result_text="you win!"+"computer picked "+computer_choice
        my_score+=1
    result_label.config(text=result_text)
    scoreboard.config(text='me'+'-->'+str(my_score)+" | "+'computer'+'-->'+str(computer_score))
root.config(background='light blue')
root.title('my first game')
game_icon=tk.Label(root,
                   text='welcome!😎😎😎😎⚔⚔⚔',
                   font=("Arial",25),
                   image=icon,
                   compound='bottom',
                   bg='green')
game_icon.pack()
scoreboard=tk.Label(root,text='me-->0 | computer-->0',height=3,width=20,font=('Arial',15),bg='grey')
scoreboard.pack()
rock=tk.Button(root,
               text="Rock",
               font=("Arial",25),
               bg='orange',
               width=15,
               command=lambda:play('rock'),activebackground='orange')
rock.pack()
paper=tk.Button(root,
                text="Paper",
                font=("Arial",25),
                bg='orange',
                width=15,
                command=lambda:play('paper'),activebackground='orange')
paper.pack()
scissors=tk.Button(root,
                   text='scissors',
                   font=("Arial",25),
                   bg='orange',
                   width=15,
                   command=lambda:play('scissors'),activebackground='orange')
scissors.pack()

result_label=tk.Label(root,text="",font=('Arial',30),bg='navy',fg='yellow')
result_label.pack()
root.mainloop()



















    

