from tkinter import *

root=Tk()
root.geometry("2000x1000")
root.configure(bg="lightblue")
root.title("Greeting")
inp =Label(root,text="hello")
f1=Frame(root, bg="blue",width=200, height=100 ).pack()
inp.pack()
root.mainloop()