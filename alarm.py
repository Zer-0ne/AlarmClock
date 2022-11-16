
from concurrent.futures import thread
import datetime
import multiprocessing
from playsound import playsound
import playsound
import os
from time import strftime
from tkinter import *
from time import sleep
from time import time
import time
import calendar
from tkinter import messagebox
from threading import *
from multiprocessing import *



clock = Tk()
clock.title('SahilKhan Alarm Clock')
# clock.geometry('500x340')
clock.resizable(False,False)
clock.configure(bg='black')

def Threading():
    t = []
    t1=t.append(Thread(target=alarm))
    t2 = t.append(Thread(target=time))
    t.start()

def time(): 
    string = strftime('%H:%M:%S') 
    lbl.config(text = string) 
    lbl.after(1000, time) 

date = datetime.datetime.now()
format_date = f"{date:%a, %b %d %Y}"
w = Label(clock, text=format_date, font = ('calibri', 40, 'bold'), 
            background = 'black', 
            foreground = 'green').pack()

# Styling the label widget so that clock 
# will look more attractive 
lbl = Label(clock, font = ('calibri', 40, 'bold'), 
            background = 'black', 
            foreground = 'green') 

# Placing clock at the centre 
# of the tkinter window 
lbl.pack(anchor = 'center',fill='x',ipady=2)  

def alarm(set_alarm_timer):
    while True:
        current_time = datetime.datetime.now()
        now = current_time.strftime("%T")
        date = current_time.strftime('%D')
        string = strftime('%H:%M:%S') 
        lbl.config(text = string) 
        lbl.after(1000, time)
#        print('The Set Date is:',date)
#        print(now)
        time()
        sleep(1)
        if now == set_alarm_timer:
            # file = 'fajar_alarm.mp3'
            # playsound(os.system('fajar_alarm.mp3'))
            playsound.playsound('/mnt/1A10343510341A69/sahil/my C language/Python/MyPractice/gui/alram/gun.mp3')
            messagebox.showinfo('Time up','Time up!!')
            # os.startfile('fajar_alarm.mp3')
            break

def actual_time():
    h = hour.get()
    m = min.get()
    s = sec.get()
    if len(h)==0 or len(m)==0 or len(s)==0:
        a = messagebox.showinfo("Error","No text input!!").pack()
    else:
        set_alarm_timer = f'{hour.get()}:{min.get()}:{sec.get()}'
        alarm(set_alarm_timer)
        time()

# def difference(set_alarm_timer):
      
#     # convert h1 : m1 into
#     # minutes
#     t1 = datetime.datetime.now()
#     t2 = actual_time()
#     # set = h1 * 60 + m1
      
#     # convert h2 : m2 into
#     # minutes 
#     # t2 = h2 * 60 + m2
      
#     # if (t1 == t2): 
#     #     print("Both are same times")
#     #     return 
#     # else:
          
#     #     # calculating the difference
#     diff = t2-t1
          
#     # # calculating hours from
#     # # difference
#     # h = (int(diff / 60)) % 24
      
#     # # calculating minutes from 
#     # # difference
#     # m = diff % 60

hour = StringVar()
min = StringVar()
sec = StringVar()
border_color = Frame(clock, background="red").pack(padx=1,pady=1,fill='x') 
time_format = Label(border_color,text='Enter time in 24 hour format!',fg='red',bg='black',font="Arial 16 bold").pack(fill='x',ipady=3)

hourTime = Entry(clock,textvariable=hour,bg='black',highlightcolor='green',fg='green', font='arial 15',highlightbackground='black',width='14',insertbackground='green')
hourTime.place(x=5,y=183)
minTime = Entry(clock,textvariable=min,bg='black',highlightcolor='green',fg='green', font='arial 15',highlightbackground='black',width='14',insertbackground='green').pack(pady=7)
secTime = Entry(clock,textvariable=sec,bg='black',highlightcolor='green',fg='green', font='arial 15',highlightbackground='black',width='14',insertbackground='green').place(x=335,y=183)


hourTime.insert(10, "Hours")
# minTime.INSERT(10, "Hours")
time_format = Label(clock,text='    ',fg='red',bg='black',font="Arial").pack(fill='x',ipady=0)

submit = Button(time_format,text = "Set Alarm",fg="green",bg='black',width = 5,command = actual_time,highlightcolor='green', font='arial 15',highlightbackground='black').pack(ipadx=130)
time_format = Label(clock,text='    ',fg='red',bg='black',font="Arial").pack(fill='x',ipady=0)
# border_color = Frame(clock, background="red").pack(padx=1,pady=5,fill='x')
Label(border_color,text='SahilKhan',font='arial 22 bold', bg='red',fg='black',width='20').pack(side='bottom',ipady=3,fill='x')

time()

clock.mainloop()
