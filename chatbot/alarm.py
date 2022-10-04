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
        n_TimeEnd = Time_text.get()
        print(n_TimeEnd)
        n_Reminder = Reminder_text.get()
        print(n_Reminder)

        try:
            c_TimeEnd = int(n_TimeEnd) * 60

            if c_TimeEnd < 0:
                messagebox.showinfo(message="Error.., n >= 0, and n cannot be decimal (e.g. 0.1)")

            elif c_TimeEnd >= 0:
                if n_Reminder == "":
                    n_Reminder = "Time's up!"

                root.state('icon')
                event.wait(c_TimeEnd)
                NowTime = datetime.datetime.now()
                NowTime = str(NowTime)
                NowTime = NowTime[0:19]
                messagebox.showinfo(title="Reminder", message="Bot Reminder: \n" + "--- " + n_Reminder + " ---" + "\n" + NowTime)
        
            else:
                messagebox.showinfo(message="Error.., n >= 0, and n cannot be decimal (e.g. 0.1)")

        except ValueError:
            messagebox.showinfo(message="Error.., n >= 0, and n cannot be decimal (e.g. 0.1)")

    Button(root, text="Start :))", command = on_check).pack()

    root.mainloop()

if __name__ == "__main__":    
    ala = launchAlarm()
    ala.on_check()


    
    