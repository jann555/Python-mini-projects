"""
https://tkdocs.com/tutorial/widgets.html#entry
https://replit.com/@appbrewery/grid-columnspan-demo#main.py
https://tkdocs.com/tutorial/canvas.html
"""
import json
from json import JSONDecodeError
from tkinter import Tk, Button, Label, Canvas, PhotoImage, Entry, END, messagebox
import pyperclip
import password_generator as password_manager

FILE_NAME = "saved_passwords.json"


def search_website():
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            # Retrieve new data
            website = data[website_entry.get()]
            email = website["email"]
            password = website["password"]
    except FileNotFoundError:
        messagebox.showerror("404", "File Not Found")
    except KeyError:
        messagebox.showerror("404", "Website Not Found")
    else:
        # clear fields
        email_username_entry.delete(0, END)
        password_entry.delete(0, END)
        # Replace with new data
        password_entry.insert(0, password)
        email_username_entry.insert(0, email)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password = password_manager.random_password()
    pyperclip.copy(password)
    password_entry.insert(0, password)
    pass


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror("ERROR", "Required fields empty!")
    else:
        try:
            with open(FILE_NAME, "r") as file:
                # Reading old Data
                data = json.load(file)

        except JSONDecodeError:
            with open(FILE_NAME, "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open(FILE_NAME, "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
                messagebox.showinfo("Success", "Password Saved Successfully")

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, highlightthickness=0)

logo_img = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_img)

# Labels and Entries
website_label = Label(text="Website:", font=("Arial", 10, "normal"))
website_entry = Entry(width=30)
website_entry.focus()
email_username_label = Label(text="Email/Username:", font=("Arial", 10, "normal"))
email_username_entry = Entry(width=50)
email_username_entry.insert(0, "dummyemail@gmail.com")
password_label = Label(text="Password:", font=("Arial", 10, "normal"))
password_entry = Entry(width=30)

# Buttons
generate_pw_button = Button(text="Generate Password", width=16, command=generate_password)
add_pw_button = Button(text="Add", width=42, command=add_password)
search_button = Button(text="Search", width=16, command=search_website)

# Grid Layout
canvas.grid(column=1, row=0)

# Labels
website_label.grid(column=0, row=1)
email_username_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

# Entries
website_entry.grid(column=1, row=1)
email_username_entry.grid(column=1, row=2, columnspan=2)
password_entry.grid(column=1, row=3)

# Buttons
generate_pw_button.grid(column=2, row=3)
add_pw_button.grid(column=1, row=4, columnspan=2)
search_button.grid(column=2, row=1)

window.mainloop()
