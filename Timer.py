from tkinter import *
from playsound import playsound
from tkinter.font import Font  
import time
import threading

# root is an object
root = Tk()
root.title("Timer")
root.geometry("450x600")
root.config(bg="black")
root.resizable(False, False)

# font style
myfont = Font(family="arial", size="35", weight="bold") 

# header label
heading = Label(root, text="TIMER", font=myfont, bg="#000", fg="#ea3548")
heading.pack(pady=40)

l = Label(root, text="CURRENT TIME  : ", font=(myfont, 15), bg="#000", fg="green").place(x=70, y=140)

def clock():
    current_time = time.strftime('%H:%M:%S %p')
    time_label.config(text=current_time)
    time_label.after(1000, clock)

time_label = Label(root, font=(myfont, 15), text=" ", fg="green", bg="#000")
time_label.place(x=245, y=140)
clock()

# timer
hrs = StringVar()
Entry(root, textvariable=hrs, width=2, font="arial 50", bg="#000", fg="#fff", bd=0).place(x=60, y=200)
hrs.set("00")

mins = StringVar()
Entry(root, textvariable=mins, width=2, font="arial 50", bg="#000", fg="#fff", bd=0).place(x=180, y=200)
mins.set("00")

sec = StringVar()
Entry(root, textvariable=sec, width=2, font="arial 50", bg="#000", fg="#fff", bd=0).place(x=300, y=200)
sec.set("00")

Label(root, text="hours", font=(myfont, 12), bg="#000", fg="#fff").place(x=135, y=245)
Label(root, text="min", font=(myfont, 12), bg="#000", fg="#fff").place(x=255, y=245)
Label(root, text="sec", font=(myfont, 12), bg="#000", fg="#fff").place(x=375, y=245)

timer_running = False
alarm_playing = False

def play_alarm():
    global alarm_playing
    alarm_playing = True
    while alarm_playing:
        playsound("Timer/alarm.wav")

def Timer_start():
    global timer_running
    timer_running = True
    times = int(hrs.get())*3600 + int(mins.get())*60 + int(sec.get())

    def countdown():
        nonlocal times
        if times >= 0 and timer_running:
            minute, second = divmod(times, 60)
            hour, minute = divmod(minute, 60)

            sec.set(f"{second:02d}")
            mins.set(f"{minute:02d}")
            hrs.set(f"{hour:02d}")

            if times == 0:
                alarm_thread = threading.Thread(target=play_alarm)
                alarm_thread.start()
            else:
                times -= 1
                root.after(1000, countdown)

    countdown()

def reset_timer():
    global timer_running, alarm_playing
    timer_running = False
    alarm_playing = False
    hrs.set("00")
    mins.set("00")
    sec.set("00")

def stop_timer():
    global timer_running, alarm_playing
    timer_running = False
    alarm_playing = False

def breakt():
    hrs.set("00")
    mins.set("15")
    sec.set("00")

def study():
    hrs.set("00")
    mins.set("25")
    sec.set("00")

def workout():
    hrs.set("01")
    mins.set("15")
    sec.set("00")

Image1 = PhotoImage(file="Timer/break.png")
button1 = Button(root, image=Image1, bg="#000", bd=0, command=breakt)
button1.place(x=25, y=300)

Image2 = PhotoImage(file="Timer/study.png")
button2 = Button(root, image=Image2, bg="#000", bd=0, command=study)
button2.place(x=160, y=300)

Image3 = PhotoImage(file="Timer/workout.png")
button3 = Button(root, image=Image3, bg="#000", bd=0, command=workout)
button3.place(x=290, y=300)

submit_Button = Button(root, text="Start", bg="green", bd=0, fg="black", width=20, height=2, font="arial 10 bold", command=Timer_start)
submit_Button.pack(padx=5, pady=40, side=BOTTOM)

reset_Button = Button(root, text="Reset", bg="#F0E072", bd=0, fg="black", width=15, height=2, font="arial 10 bold", command=reset_timer)
reset_Button.pack()
reset_Button.place(x=250, y=450)

stop_Button = Button(root, text="Stop", bg="#ea3548", bd=0, fg="black", width=15, height=2, font="arial 10 bold", command=stop_timer)
stop_Button.pack()
stop_Button.place(x=90, y=450)

root.mainloop()


