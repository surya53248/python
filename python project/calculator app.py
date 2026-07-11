import tkinter as tk
root=tk.Tk()
calculation=""


def add_to_calculation(symbol):
    global calculation
    calculation+=str(symbol)
    text_result.delete(1.0,'end')
    text_result.insert(1.0,calculation,'right_align')

def evaluate_calculation(event=None):
    global calculation
    try:
        calculation=str(eval(calculation))
        text_result.delete(1.0,'end')
        text_result.insert(1.0,calculation,'right_align')
    except:
        text_result.delete(1.0,'end')
        text_result.insert(1.0,"Error",'right_align')
        calculation=""

def clear_field(event=None):
    global calculation
    calculation=""
    text_result.delete(1.0,'end')

root.configure(bg="#1C1C1C")
root.title('A Simple Calculator')
root.geometry('300x263')
root.resizable(False,False)
tk.Label(root,text="",bg='#1C1C1C',height=1).grid(row=0,column=0)
text_result=tk.Text(root,height=2,width=22,font=('Arial',18),bg='#1C1C1C',fg='#D4D4D2')
text_result.grid(row=1,columnspan=4)
text_result.tag_configure('right_align',justify="right")
btn1=tk.Button(root,text='7',font=('Arial',17),width=5,command=lambda:add_to_calculation(7),fg='#D4D4D2',bg='#1C1C1C')
btn1.grid(row=2,column=0)
btn2=tk.Button(root,text='8',font=('Arial',17),width=5,command=lambda:add_to_calculation(8),fg='#D4D4D2',bg='#1C1C1C')
btn2.grid(row=2,column=1)
btn3=tk.Button(root,text='9',font=('Arial',17),width=5,command=lambda:add_to_calculation(9),fg='#D4D4D2',bg='#1C1C1C')
btn3.grid(row=2,column=2)
btn4=tk.Button(root,text='+',font=('Arial',17),width=5,command=lambda:add_to_calculation('+'),bg='#FF9500',fg='#D4D4D2')
btn4.grid(row=2,column=3)
btn5=tk.Button(root,text='4',font=('Arial',17),width=5,command=lambda:add_to_calculation(4),fg='#D4D4D2',bg='#1C1C1C')
btn5.grid(row=3,column=0)
btn6=tk.Button(root,text='5',font=('Arial',17),width=5,command=lambda:add_to_calculation(5),fg='#D4D4D2',bg='#1C1C1C')
btn6.grid(row=3,column=1)
btn7=tk.Button(root,text='6',font=('Arial',17),width=5,command=lambda:add_to_calculation(6),fg='#D4D4D2',bg='#1C1C1C')
btn7.grid(row=3,column=2)
btn8=tk.Button(root,text='-',font=('Arial',17),width=5,command=lambda:add_to_calculation('-'),bg='#FF9500',fg='#D4D4D2')
btn8.grid(row=3,column=3)
btn9=tk.Button(root,text='1',font=('Arial',17),width=5,command=lambda:add_to_calculation(1),fg='#D4D4D2',bg='#1C1C1C')
btn9.grid(row=4,column=0)
btn10=tk.Button(root,text='2',font=('Arial',17),width=5,command=lambda:add_to_calculation(2),fg='#D4D4D2',bg='#1C1C1C')
btn10.grid(row=4,column=1)
btn11=tk.Button(root,text='3',font=('Arial',17),width=5,command=lambda:add_to_calculation(3),fg='#D4D4D2',bg='#1C1C1C')
btn11.grid(row=4,column=2)
btn12=tk.Button(root,text='*',font=('Arial',17),width=5,command=lambda:add_to_calculation('*'),bg='#FF9500',fg='#D4D4D2')
btn12.grid(row=4,column=3)
btn13=tk.Button(root,text='c',font=('Arial',17),width=5,command=clear_field,fg='#D4D4D2',bg='#1C1C1C')
btn13.grid(row=5,column=0)
btn14=tk.Button(root,text='0',font=('Arial',17),width=5,command=lambda:add_to_calculation(0),fg='#D4D4D2',bg='#1C1C1C')
btn14.grid(row=5,column=1)
btn15=tk.Button(root,text='=',font=('Arial',17),width=5,command=evaluate_calculation,fg='#D4D4D2',bg='#1C1C1C')
btn15.grid(row=5,column=2)
btn16=tk.Button(root,text='/',font=('Arial',17),width=5,command=lambda:add_to_calculation('/'),bg='#FF9500',fg='#D4D4D2')
btn16.grid(row=5,column=3)

root.mainloop()