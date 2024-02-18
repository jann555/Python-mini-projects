"""
https://tkdocs.com/tutorial/widgets.html#entry
https://replit.com/@appbrewery/grid-columnspan-demo#main.py
https://tkdocs.com/tutorial/canvas.html
"""
from tkinter import Tk, Button, Label, Canvas, PhotoImage, Entry, END, messagebox
import password_generator as password_manager


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password = password_manager.random_password()
    password_entry.insert(0, password)
    pass


def add_password():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror("ERROR", "Required fields empty!")
    else:
        is_ok_to_save = messagebox.askokcancel(title=website, message=f"Details Entered: \nEmail: {email} "
                                                                      f"\nPassword: {password} \nIs it ok to save?")
        if is_ok_to_save:
            with open("saved_passwords.txt", "a") as file:
                entry = f' {website} | {email} | {password} \n'
                file.write(entry)
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            messagebox.showinfo("Success", "Password Saved Successfully")


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
website_entry.focus()
email_username_label = Label(text="Email/Username:", font=("Arial", 10, "normal"))
email_username_entry = Entry(width=50)
email_username_entry.insert(0, "dummyemail@gmail.com")
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
