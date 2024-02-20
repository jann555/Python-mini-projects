"""
 https://docs.python.org/3/library/tkinter.html#the-packer
 https://tcl.tk/man/tcl8.6/TkCmd/pack.htm
"""
import tkinter


def add(*args):
    return sum(args)


def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


kw_result = calculate(4, add=3, multiply=3)

window = tkinter.Tk()
window.title('First GUI Program')
window.minsize(width=500, height=300)
result = add(2, 5, 7, 8)
my_label = tkinter.Label(text=f"New Text", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)


def click():
    msg = tk_input.get()
    my_label.config(text=msg)


button = tkinter.Button(text="click me", command=click)
button.place(x=220, y=100)

# Entry

tk_input = tkinter.Entry(width=10)
tk_input.grid(column=10, row=10)

window.mainloop()
