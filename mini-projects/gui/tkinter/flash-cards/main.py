from tkinter import PhotoImage, Canvas, Button, Tk

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)

# Images from file
card_front = PhotoImage(file='./images/card_front.png')
card_back = PhotoImage(file='./images/card_back.png')
right = PhotoImage(file='./images/right.png')
wrong = PhotoImage(file='./images/wrong.png')

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR)
canvas.create_image(400, 263, image=card_front)
canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


# Buttons commands
def right_command():
    pass


def wrong_command():
    pass


# Buttons
wrong_button = Button(image=wrong, highlightthickness=0, command=wrong_command)
wrong_button.grid(row=1, column=0)
right_button = Button(image=right, highlightthickness=0, command=right_command)
right_button.grid(row=1, column=1)
window.mainloop()
