"""
 https://docs.python.org/3/library/tkinter.html#the-packer
 https://tcl.tk/man/tcl8.6/TkCmd/pack.htm
 https://tcl.tk/man/tcl8.6/TclCmd/after.htm
"""

from tkinter import Tk, Button, Label, Canvas, PhotoImage

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW, highlightthickness=0)
timer_label = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
check_label = Label(text='✔️', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
tomato_img = PhotoImage(file='tomato.png')

canvas = Canvas(width=200, height=224)
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, "bold"))
canvas.config(bg=YELLOW)

start_button = Button(text="Start")
reset_button = Button(text="Reset")

# Grid layout
timer_label.grid(column=1, row=0)
canvas.grid(column=1, row=1)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)
check_label.grid(column=1, row=3)


window.mainloop()
