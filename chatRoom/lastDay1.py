from tkinter import *
import time

root = Tk()

timer = Label(root, font=('Tahoma', 80), width=6, height=2)
timer.pack()
counter = 0

def start():
    global counter
    if counter < 100:
        counter += 1
        name = str(counter)
        time.sleep(1)
        timer.config(text=name)
    global time_increase
    time_increase = timer.after(50, start)

def reset():
    global counter
    counter = 0
    name = str(counter)
    timer.config(text=name)

def stop():
    root.after_cancel(time_increase)


button1 = Button(root, text="timer start", command=start)
button1.place(x=0, y=0)

button2 = Button(root, text="timer reset", command=reset)
button2.place(x=150, y=0)

button3 = Button(root, text="timer stop", command=stop)
button3.place(x=300, y=0)

root.mainloop()

