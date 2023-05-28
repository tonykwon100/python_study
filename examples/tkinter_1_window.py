import requests
from tkinter import *
from datetime import datetime
from bs4 import BeautifulSoup


win = Tk()

def winexit():
    win.destroy()
    win.quit()
    exit()

def setup():
    value = ent.get()
    print(value)

print(datetime.now())
win.geometry("500x500")
win.title("temp...제목")
win.option_add("*Font","맑은고딕 25")

btn = Button(win, text = "Exit", command = winexit, width=10, height=10)
btn_setup = Button(win, text = "Setup", command = setup, width=10, height=10)

ent = Entry(win)
ent.pack()

btn.pack()
btn_setup.pack()


win.configure(bg="black")
win.wm_attributes('-fullscreen', 'True')

url = "https://dhlottery.co.kr/gameResult.do?method=byWin"
req = requests.get(url)

soup = BeautifulSoup(req.text, "html.parser")
txt = soup.find("div", attrs = {"class","win_result"}).get_text()

print(txt)
num_list = txt.split("\n")[7:13]
print(num_list)


win.mainloop()
