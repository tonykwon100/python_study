from tkinter import *
from selenium import webdriver    # for login

win = Tk()
win.title("Daum Log-in")
win.geometry("400x300")
win.option_add("*Font", "궁서 20")

lab_d = Label(win)
img = PhotoImage(file = "E:\pythonwork\greentea_ice_flakes.png", master = win)
img = img.subsample(8)
lab_d.config(image = img)
lab_d.pack()

lab1 = Label(win)
lab1.config(text="ID")
lab1.pack()
ent1 = Entry(win)
ent1.insert(0, "hong@gmail.com")
def clear(event):
    if ent1.get() == "hong@gmail.com":
      ent1.delete(0, len(ent1.get()))
ent1.bind("<Button-1>", clear)
ent1.pack()

lab2 = Label(win)
lab2.config(text="Password")
lab2.pack()
ent2 = Entry(win)
ent2.config(show = "*")
ent2.pack()

btn = Button(win)
btn.config(text="Log in")
def login():
  my_id = ent1.get()
  my_pw = ent2.get()
  print(my_id, my_pw)
  lab3.config(text = "[MSG] login success.")
  ################# login code.. need chromedriver....
  driver = webdriver.Chrome("E:/pythonwork/chromdriver")
  url = "https://accounts.kakao.com/login/?continue=https%3A%2F%2Flogins.daum.net%2Faccounts%2Fksso.do%3Frescue%3Dtrue%26url%3Dhttps%253A%252F%252Fwww.daum.net#login"
  driver.get(url)
  driver.implicitly_wait(5)
  xpath1 = "//input[@name='loginKey']"
  driver.find_element("xpath", xpath1).send_keys(my_id)
  driver.implicitly_wait(5)
  xpath2 = "//input[@name='password']"
  driver.find_element("xpath", xpath2).send_keys(my_pw)
  driver.implicitly_wait(5)
  xpath3 = "//button[@class='btn_g highlight submit']"
  driver.find_element("xpath", xpath3).click()

btn.config(command = login)
btn.pack()

lab3 = Label(win)
lab3.pack()


win.mainloop()
