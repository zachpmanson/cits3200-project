from logging import root
from tkinter import *
from tkinter import ttk
import tkinter as tk

def create_window(getReply):

    # Menu buttons not fuunctioning
    # Messages in chat_window need to be from bottom up
    # Bot messages in chat_window need to be alligned right hand side
    # message_window not returning cursor to top left

    # parent window
    main_window = tk.Tk()
    main_window.title("Chat Bot v0.1") # window name
    main_window.geometry("400x500+100+100") # dimensions + Location; Width x Height + x + y axis
    main_window.resizable(width=False, height=False) # disable window resize


    # get input function
    def send(input):       
        msg = message_window.get("1.0", END).strip()
        reply = getReply(msg)
        print(f"User: {msg}")
        print(f"Bot: {reply}")
        chat_window.configure(state="normal") # allows inserting into window
        chat_window.insert(END, f"\nUser: {msg}")
      
        # chat_window.tag_configure("right", justify='right') # configures window to input text right alligned
        # chat_window.tag_add("right", 1.0, "end")

        chat_window.insert(END, f"\nBot: {reply}")


        chat_window.configure(state="disabled") # disables users for inputting directly into window
        message_window.delete("1.0", END) # clears message_window after msg is sent

    # chat window
    chat_window = Text(main_window, bd=1, bg="Grey", width =50, height = 8, cursor="arrow", wrap=WORD)
    chat_window.place(x=6, y=6, height= 414, width= 388)
    chat_window.configure(state="disabled") # disables users for inputting directly into window

    # message window
    message_window = Text(main_window, bg="grey", width=30, cursor="arrow", wrap=WORD)
    message_window.bind("<Return>", send)
    message_window.place(x=6, y=426, height=68, width=388)

    # main menu bar - possibly delete
    main_menu = Menu(main_window)

    # sub menu - possibly delete
    file_menu = Menu(main_window)
    file_menu.add_command(label="Test 1")
    file_menu.add_command(label="Test 2")
    file_menu.add_command(label="Test 3")

    # main menu widgets - possibly delete
    main_menu.add_cascade(label="Drop Down", menu = file_menu) 
    main_menu.add_command(label="Log Out") 
    main_menu.add_command(label="Button 3") 
    main_window.config(menu=main_menu) 



    return main_window
    #main_window.mainloop()

if __name__=="__main__":
    window = create_window(lambda x: "Placeholder reply funtion")
    window.mainloop()