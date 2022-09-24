from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label1.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = int(WORK_MIN * 60)
    short_break = int(SHORT_BREAK_MIN * 60)
    long_break = int(LONG_BREAK_MIN * 60)

    if reps >= 9:
        reset_timer()
    elif reps == 8:
        # For 8th rep
        count_down(long_break)
        label1.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        # For 2nd/4th/6th rep
        count_down(short_break)
        label1.config(text="Short Break", fg=PINK)
    else:
        # For 1st/3rd/5th/7th reps
        count_down(work_sec)
        label1.config(text="Work", fg="green")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    mini = math.floor(count / 60)
    sec = count % 60
    if sec < 10:
        sec = f'0{sec}'
    if mini < 10:
        mini = f'0{mini}'
    canvas.itemconfig(timer_text, text=f"{mini}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    # Triggering the timer again
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            marks += "✅"
        check_mark.config(text=f"{marks}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title(string='Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(height=224, width=200, bg=YELLOW, highlightthickness=0)
tomato_pic = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_pic)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

label1 = Label(text='Timer', font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)
label1.grid(row=0, column=1)

start_button = Button(text='Start', width=7, highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text='Reset', width=7, highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
check_mark.grid(column=1, row=2)

window.mainloop()
