import random
from tkinter import PhotoImage, Canvas, Button, Tk

import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
learn_dictionary = {}

try:
    # LOAD DATA
    data_frame = pd.read_csv('./data/word_to_learn.csv')
except FileNotFoundError:
    data_frame = pd.read_csv('./data/french_words.csv')
    learn_dictionary = data_frame.to_dict(orient="records")
else:
    learn_dictionary = data_frame.to_dict(orient="records")


# Buttons commands
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(learn_dictionary)
    canvas.itemconfig(tittle_text, text=f'French', fill='black')
    canvas.itemconfig(card_word, text=f'{current_card['French']}', fill='black')
    canvas.itemconfig(flash_card, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(tittle_text, text=f'English', fill='white')
    canvas.itemconfig(card_word, text=f'{current_card['English']}', fill='white')
    canvas.itemconfig(flash_card, image=card_back)
    canvas.update()


def is_known():
    learn_dictionary.remove(current_card)
    data = pd.DataFrame(learn_dictionary)
    data.to_csv("./data/word_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)
# Delay 3 seconds
flip_timer = window.after(3000, func=flip_card)
# Images from file
card_front = PhotoImage(file='./images/card_front.png')
card_back = PhotoImage(file='./images/card_back.png')
right = PhotoImage(file='./images/right.png')
wrong = PhotoImage(file='./images/wrong.png')

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR)
flash_card = canvas.create_image(400, 263, image=card_front)
tittle_text = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_button = Button(image=wrong, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)
right_button = Button(image=right, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
