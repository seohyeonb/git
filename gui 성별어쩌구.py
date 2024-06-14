import tkinter as tk
from tkinter import ttk

GENDER=['남성','여성','기타']
COLOR=['red','pink','black']

def buildGUI():
    text_label=ttk.Label(win,text='당신의 성별은?')
    text_label.pack()

    global gender
    gender=tk.IntVar()
    for i in range(3):
        radio_btn=ttk.Radiobutton(win,text=GENDER[i],value=i,variable=gender,command=radio_btn_handler)
        radio_btn.pack()
        
    gender.set(-1)
    
def radio_btn_handler():
    choice=gender_get()
    win.configure(background=COLOR[choice])
    
win=tk.Tk()
win.title('버튼 위젯 예')
buildGUI()
win.mainloop()
