from tkinter import *


def on_button_click():
    km = float(miles_input.get()) * 1.609
    km_result_label.config(text=f"{km}")


# Creating a new window and configurations
window = Tk()
window.title("Miles to KM Converter")
window.config(padx=20, pady=20)

# entry
miles_input = Entry(width=7)
miles_input.insert(END, string="0")
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Labels
is_equal_label = Label(text="is Equal to")
is_equal_label.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=on_button_click)
calculate_button.grid(column=1, row=2)


window.mainloop()
