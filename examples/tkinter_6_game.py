from tkinter import *
import random
from datetime import datetime

win = Tk()
win.geometry("550x150")
win.title("game")
win.option_add("*Font", "궁서 20")

lab = Label(win)
lab.config(text="표적개수")
lab.grid(column=0,row=0,padx=20,pady=20)

ent = Entry(win)
ent.grid(column=1,row=0,padx=20,pady=20)


k = 1

def cc():
  global k
  if k < num_t:
    k += 1
    btn.destroy()
    ran_btn()
  else:
    fin = datetime.now()
    dif_sec = (fin - start).total_seconds()
    btn.destroy()
    lab = Label(win)
    lab.config(text="Clear " + str(dif_sec) + " sec.")
    lab.pack(pady=230)
    


def ran_btn():
  global btn
  btn = Button(win)
  btn.config(bg = "red")
  btn.config(command=cc)
  btn.config(text = k)
  btn.place(relx=random.random(), rely=random.random())

def btn_f():
  global num_t
  global start
  num_t = int(ent.get())
  for wg in win.grid_slaves():
    wg.destroy()
  win.geometry("500x500")
  ran_btn()
  start = datetime.now()


btn = Button(win)
btn.config(text="Start")
btn.config(command=btn_f)
btn.grid(column=0,row=1,columnspan=2)

win.mainloop()