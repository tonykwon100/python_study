from tkinter import *

win = Tk()
win.geometry("800x500")
win.title("place")
win.option_add("*Font", "궁서 20")

xx = 30
yy = 50

btn = Button(win)
btn.config(text = "({},{})".format(xx,yy))
btn.place(x=xx, y=yy)

xx = 0.5
yy = 0.5
btn1 = Button(win)
btn1.config(text = "({},{})".format(xx,yy))
btn1.place(relx=xx, rely=yy)


win.mainloop()

