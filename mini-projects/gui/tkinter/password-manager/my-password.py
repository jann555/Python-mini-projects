"""
https://tkdocs.com/tutorial/widgets.html#entry
https://replit.com/@appbrewery/grid-columnspan-demo#main.py
https://tkdocs.com/tutorial/canvas.html
"""
from tkinter import Tk, Button, Label, Canvas, PhotoImage, Entry


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass


def add_password():
    pass


# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, highlightthickness=0)

logo_img = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_img)

# Labels and Entries
website_label = Label(text="Website:", font=("Arial", 10, "normal"))
website_entry = Entry(width=50)
email_username_label = Label(text="Email/Username:", font=("Arial", 10, "normal"))
email_username_entry = Entry(width=50)
password_label = Label(text="Password:", font=("Arial", 10, "normal"))
password_entry = Entry(width=30)

# Buttons
generate_pw_button = Button(text="Generate Password", width=16, command=generate_password)
add_pw_button = Button(text="Add", width=43, command=add_password)

# Grid Layout
canvas.grid(column=1, row=0)

# Labels
website_label.grid(column=0, row=1)
email_username_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

# Entries
website_entry.grid(column=1, row=1, columnspan=2)
email_username_entry.grid(column=1, row=2, columnspan=2)
password_entry.grid(column=1, row=3)

# Buttons
generate_pw_button.grid(column=2, row=3)
add_pw_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
