import tkinter as tk #tkinter is for GUI
from time import strftime #strftime lets us to format current time and  date and we can arrange it as we want

root = tk.Tk() #this is to diplay our elements
root.title("Digital Clock by Zakir")

def time():
    string = strftime("%H:%M:%S %p\n %d/%m/%y %a") #%p is for am/pm and %a is for day name
    label.config(text=string) #updates the text inside our label to new time sting
    label.after(1000,time) #this will call label after  every second and updates time date

label = tk.Label(root, font=('calibri', 50, 'bold'), background='yellow', foreground='blue')
label.pack(anchor='center') #anchor in tkinter tells where to position a widget 

time() #calls  time function for first time
root.mainloop() #it tells python to keep the window open and running