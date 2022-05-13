from tkinter import *

window = Tk()

count = 0

def click():
    global count
    count = count +1
    print(count)

button = Button(window,
                text="Click me!",
                command=click,
                font=("Comic Sans",30),
                fg="#00ff00",
                bg="#000000",
                activeforeground="#00ff00",
                activebackground="#000000",)

button.pack()

window.mainloop()