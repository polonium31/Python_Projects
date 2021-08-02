import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
my_timer =None
cnt = 0


# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    timer.config(text="Timer")
    check_mark.config(text="No Session")
    global cnt
    cnt =0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    work_sec = WORK_MIN *60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    global cnt
    cnt += 1
    count_down(work_sec)
    if cnt % 8 == 0:
        count_down(long_break_sec)
        timer.config(text="Long Break", fg=GREEN)

    elif cnt % 2 == 0:
        count_down(short_break_sec)
        timer.config(text="Short Break", fg=PINK)

    else:
        count_down(work_sec)
        timer.config(text="Work ", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count_sec < 10:
        canvas.itemconfig(timer_text, text=f"{count_min:02}:{count_sec:02}")
    if count_sec == 0:
        count_sec = "00"
    if count > 0:
        global my_timer
        my_timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        work_session = math.floor(cnt/2)
        mark=""
        for _ in range(work_session):
            mark += "✅"
        check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
app= Label(text="Pomodoro Technic", font=(FONT_NAME, 40), fg="black", bg=YELLOW)
app.grid(row=0, column=2)
timer = Label(text="Timer", font=(FONT_NAME, 35), fg=GREEN, bg=YELLOW)
timer.grid(row=1, column=2)

canvas = Canvas(width=200, height=225, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.gif")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30))
canvas.grid(row=2, column=2)

start_btn = Button(text="start", font=(FONT_NAME, 15), highlightbackground='#3E4149', bg=YELLOW, command=start_timer)
start_btn.grid(row=3, column=0)

reset_btn = Button(text="reset", font=(FONT_NAME, 15), highlightbackground='#3E4149', bg=YELLOW,command=reset)
reset_btn.grid(row=3, column=3)

check_mark = Label(text="No session", highlightthickness=0,)
check_mark.grid(row=4, column=2)
window.mainloop()
