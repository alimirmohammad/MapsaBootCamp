from tkinter import *
import time

root = Tk()

timer = Label(root, font=('Tahoma', 80), width=6, height=2)
timer.pack()
counter = 0
counter2 = 0

# def update_clock():
#     now = time.strftime("%H:%M:%S")
#     timer.label.configure(text=now)
#     timer.root.after(1000, update_clock)


def start():
    global counter
    global counter2
    # while counter < 100:
    if counter < 100:
        # counter += 1
        
        counter2 += 1
        if counter2 >= 100:
            counter2 = 0
            counter += 1
        # time.sleep(0.01)
        name = f'{counter}.{counter2}'
        time.sleep(0.005)
        timer.config(text=name)
    global time_increase
    time_increase = timer.after(5, start)

def reset():
    global counter
    counter = 0
    name = str(counter)
    timer.config(text=name)

def stop():
    root.after_cancel(time_increase)


button1 = Button(root, text="timer start", command=start)
button1.place(x=0, y=0)
# button1 = Button(root, text="timer start", command=update_clock)
# button1.place(x=0, y=0)

button2 = Button(root, text="timer reset", command=reset)
button2.place(x=150, y=0)

button3 = Button(root, text="timer stop", command=stop)
button3.place(x=300, y=0)

root.mainloop()

