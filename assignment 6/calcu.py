from tkinter import *

root = Tk()
root.geometry("375x425")
root.configure(bg="lightblue")
root.title("Calculator")


e = Entry(root, width=20, borderwidth=5, bg="lightgreen", font=("Arial", 20))
e.grid(row=0, column=0, columnspan=4, padx=10, pady=20)



def button_click(number):
    e.insert(END, str(number))


def button_clear():
    e.delete(0, END)


def button_equal():
    try:
        result = eval(e.get())
        e.delete(0, END)
        e.insert(0, result)
    except:
        e.delete(0, END)
        e.insert(0, "Error")


buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        Button(root, text=text, width=5, height=2, font=("Arial", 18), bg="orange",
               command=button_equal).grid(row=row, column=col, padx=5, pady=5)
    elif text == "C":
        Button(root, text=text, width=5, height=2, font=("Arial", 18), bg="red",
               command=button_clear).grid(row=row, column=col, padx=5, pady=5)
    else:
        Button(root, text=text, width=5, height=2, font=("Arial", 18), bg="lightblue",
               command=lambda t=text: button_click(t)).grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
