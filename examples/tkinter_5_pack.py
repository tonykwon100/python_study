from tkinter import *

win = Tk()
win.geometry("800x500")
win.title("pack")
win.option_add("*Font", "궁서 20")

ent = Entry(win)
ent.insert(0, "right")
ent.pack(side = "top")

btn = Button(win)
btn.config(text = "Button")
def aa():
    btn.pack(side = ent.get())
btn.config(command = aa)
btn.pack()

btn2 = Button(win)
btn2.config(text = "temp")
btn2.pack(pady=50)

win.mainloop()

