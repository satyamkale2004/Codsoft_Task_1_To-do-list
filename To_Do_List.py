#import module

from tkinter import *
from tkinter import messagebox

#Create the functions
def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def deleteTask():
    lb.delete(ANCHOR)
    
#Configure and create the mainwindow  
ws = Tk()
ws.geometry('420x420')
ws.title('To Do List')
ws.config(bg='#000000')
ws.resizable(width=False, height=False)

#create widgets(entry,button,scrollbar,listbox,frame)
frame = Frame(ws)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=22,
    height=7,
    font=('Times',20),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
    
)
lb.pack(side=LEFT, fill=BOTH)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    ws,
    font=('times', 15)
    )

my_entry.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Enter Task',
    font=('times 12'),
    bg='#c5f776',
    padx=20,
    pady=3,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 12'),
    bg='#ff8b85',
    padx=20,
    pady=3,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


ws.mainloop()