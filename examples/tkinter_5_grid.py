from tkinter import *

win = Tk()
win.geometry("800x500")
win.title("grid")
win.option_add("*Font", "궁서 20")


# btn1 = Button(win)
# btn1.config(text = "(0,0)")
# btn1.grid(column=0, row=0)

# btn2 = Button(win)
# btn2.config(text = "(1,0)")
# btn2.grid(column=1, row=0)

# btn3 = Button(win)
# btn3.config(text = "(0,1)")
# btn3.grid(column=0, row=1)

# btn4 = Button(win)
# btn4.config(text = "(0,3)")
# btn4.grid(column=0, row=3)

col_num = 4
row_num = 3
btn_list = []
for j in range(0,row_num):
    for i in range(0,col_num):
        btn = Button(win)
        btn.config(text= "({},{})".format(i,j))
        btn.grid(column=i,row=j,padx=10,pady=10)
        btn_list.append(btn)

btn = Button(win)
btn.config(text = "new")
btn.grid(column=3, row=0, rowspan=2)

btn2 = Button(win)
btn2.config(text = "new")
btn2.grid(column=1, row=2, columnspan=2)

win.mainloop()

