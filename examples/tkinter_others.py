from tkinter import *
from tkinter.ttk import *   ## for Combobox

win = Tk()
win.geometry("500x800")
win.option_add("*Font", "Arial 20")

######## Listbox
lb = Listbox(win)
# lb.config(selectmode="multiple")
lb.insert(0,"No.1")
lb.insert(1,"No.2")
lb.insert(2,"No.3")
lb.pack()

def click():
    text1 = "{}".format(lb.curselection()[0]) + " " + "{}".format(cv1.get()) + " " + "{}".format(rv.get()) + " " + cb.get()
    print(text1)
    lab.config(text=text1)
    print(scale.get())

btn = Button(win)
btn.config(text="option selection")
btn.config(command=click)
btn.pack()

lab = Label(win)
lab.pack()

######## Check button
cv1 = IntVar()
cv2 = IntVar()
cb1 = Checkbutton(win, text="No1", variable=cv1)
cb2 = Checkbutton(win, text="No2", variable=cv2)
cb1.pack(side="left")
cb2.pack(side="left")

######### Radio button
rv = IntVar()
rb1 = Radiobutton(win, text="No1", value=0, variable=rv)
rb2 = Radiobutton(win, text="No2", value=1, variable=rv)
rb3 = Radiobutton(win, text="No3", value=2, variable=rv)
rb1.pack()
rb2.pack()
rb3.pack()

###### Combobox
cb_list = ["1", "2", "3"]
cb = Combobox(win)
cb.config(values=cb_list)
cb.pack()

##### Spinbox
sb = Spinbox(win)
sb.config(from_ = -1, to = 1)
sb.pack()

#### Scale
scale = Scale(win)
scale.config(length=100, from_=0, to = 50, orient="horizontal")
scale.pack()

win.mainloop()