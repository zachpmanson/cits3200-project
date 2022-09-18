import datetime
from tkinter import *
from tkinter import messagebox
import threading

def launchAlarm():
    root = Tk()
    root.wm_attributes('-topmost',1)
    root.title("Alarm")
    root.geometry("300x150")

    l1 = Label(root, text="Set Time (Minutes)")
    l1.pack()
    xls_text = StringVar()
    xls = Entry(root, textvariable = xls_text)
    xls_text.set("")
    xls.pack()

    l2 = Label(root, text="What shall I remind you about? (Option)")
    l2.pack()
    Reminder_text = StringVar()
    Reminder = Entry(root, textvariable = Reminder_text)
    Reminder_text.set("")
    Reminder.pack()


    def on_check():
        event = threading.Event()
        NowTime = datetime.datetime.now()
        TimeEnd = xls_text.get()
        TimeEnd = int(TimeEnd) * 60
        Reminder = Reminder_text.get()

        if TimeEnd < 0:
            print(TimeEnd)
            messagebox.showinfo(message="Error.., n >= 0, and n cannot be decimal (e.g. 0.1)")
         
        else:
            if Reminder == "":
                Reminder = "Time's up!"
            NowTime = str(NowTime)
            NowTime = NowTime[0:19]
            print("Time now: ", NowTime)

            event.wait(TimeEnd)
            messagebox.showinfo(title="Reminder", message=Reminder+ "\n" + NowTime)

    Button(root, text="Start :))", command = on_check).pack()

    root.mainloop()

if __name__ == "__main__":    

    launchAlarm()

    
    