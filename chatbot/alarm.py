import datetime
from tkinter import *
from tkinter import messagebox
import threading
#import re

def launchAlarm():
    root = Tk()
    root.wm_attributes('-topmost',1)
    root.title("Alarm")
    root.geometry("300x150")

    l1 = Label(root, text="Set Time (Minutes)")
    l1.pack()
    Time_text = StringVar()
    Timer = Entry(root, textvariable = Time_text)
    Time_text.set("0")
    Timer.pack()

    l2 = Label(root, text="What shall I remind you about? (Option)")
    l2.pack()
    Reminder_text = StringVar()
    Reminder = Entry(root, textvariable = Reminder_text)
    Reminder_text.set("")
    Reminder.pack()


    def on_check():
        event = threading.Event()
        NowTime = datetime.datetime.now()

        TimeEnd = Time_text.get()
        TimeEndInt = int(TimeEnd) * 60
        Reminder = Reminder_text.get()
        #try:
        #    TimeEnd = Time_text.get()
        #    TimeEnd = int(TimeEnd) * 60
            
        #except ValueError:
        #    pass
        #TimeEnd = Time_text.get()
        #TimeEnd = int(float(TimeEnd)) * 60
        #if TimeEnd == 0:
        #    TimeEnd = 0
        #elif TimeEnd > 0:
        #    TimeEnd = TimeEnd * 60

        #Reminder = Reminder_text.get()
        #TimeEnd = re.findall(r'\d+\.\d+', TimeEnd)

        if TimeEndInt < 0:
            messagebox.showinfo(message="Error.., n >= 0, and n cannot be decimal (e.g. 0.1)")

        else:
            if Reminder == "":
                Reminder = "Time's up!"
            NowTime = str(NowTime)
            NowTime = NowTime[0:19]
            print("Time now: ", NowTime)

            root.state('icon')
            event.wait(TimeEndInt)
            messagebox.showinfo(title="Reminder", message="Bot Reminder: \n" + Reminder+ "\nNOW!\n" + str(datetime.datetime.now()))

    Button(root, text="Start :))", command = on_check).pack()

    root.mainloop()

if __name__ == "__main__":    

    launchAlarm()


    
    