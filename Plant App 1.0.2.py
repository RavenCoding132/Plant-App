import tkinter as tk
import webbrowser
import time

window = tk.Tk()
window.title("App")
window.minsize(300,121)

def handle_keypress(event):
    print(event.char)

def action_1(event):
    print("Button 1 clicked!")
    button1.configure(text="Button 4")


def action_2(event):
    print("Button 2 clicked!")

def action_3(event):
    print("Button 3 clicked!")

# rows
row1 = tk.Frame()
row2 = tk.Frame()

# columns
frame1 = tk.Frame(master=row2, width=10)
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
frame1.pack_propagate(False)

frame2 = tk.Frame(master=row2, width=10)
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame3 = tk.Frame(master=row2, width=10)
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

title1 = tk.Label(master=row1, text="Which option would you like to choose?")
title1.pack()

# elements
button1 = tk.Button(master=frame1, text="Action 1")
button1.bind("<Button-1>", action_1)
button1.place(relx=0.5, rely=0.5, anchor='center')

button2 = tk.Button(master=frame2, text="Action 2")
button2.bind("<Button-1>", action_2)
button2.place(relx=0.5, rely=0.5, anchor='center')

button3 = tk.Button(master=frame3, text="Action 3")
button3.bind("<Button-1>", action_3)
button3.place(relx=0.5, rely=0.5, anchor='center')

w = 350
h = 110
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
window.geometry('%dx%d+%d+%d' % (w, h, x, y))

row1.pack(fill=tk.X, expand=False)
row2.pack(fill=tk.BOTH, expand=True)

window.bind("<Key>", handle_keypress)

window.mainloop()