import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25  # 1 3 5 7
SHORT_BREAK_MIN = 5  # 2 4 6
LONG_BREAK_MIN = 20  # 8
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    top_label.config(text='Pomodoro', font=(FONT_NAME, 50, 'bold'), bg=YELLOW, fg=GREEN)
    bottom_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    print(reps)
    if reps % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        top_label.config(text='Short Break', fg=RED)
    elif reps % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        top_label.config(text='Long Break', fg=PINK)
    else:
        countdown(WORK_MIN * 60)
        top_label.config(text='Work', fg=GREEN)



    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = (count % 60)

    canvas.itemconfig(timer_text, text=f"{str(count_min).zfill(2)}:{str(count_sec).zfill(2)}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✓"
            bottom_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(column=1, row=1)

timer_text = canvas.create_text(103, 130, text=f'00:00', fill='white', font=(FONT_NAME, 35, 'bold'))

top_label = tkinter.Label(text='Pomodoro', font=(FONT_NAME, 50, 'bold'), bg=YELLOW, fg=GREEN)
top_label.grid(column=1, row=0)

bottom_label = tkinter.Label(bg=YELLOW, fg=GREEN)
bottom_label.grid(column=1, row=3)

button_start = tkinter.Button(text='Start', highlightthickness=0, command=start_timer)
button_start.configure(highlightbackground=YELLOW)
button_start.grid(column=0, row=2)

button_reset = tkinter.Button(text='Reset', highlightthickness=0, command=reset_timer)
button_reset.configure(highlightbackground=YELLOW)
button_reset.grid(column=2, row=2)

window.mainloop()
