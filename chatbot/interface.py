from logging import root
from tkinter import *
from tkinter import ttk

def create_window(getReply):

    # Scroll wheel + Enter Button + Menu Buttons are NON-Functioning, not sure if required.
    # Using basic responses to test user & bot responses
    # Can currently type directly into  chat_window - need to fix
    # Messages in chat_window need to be from bottom up
    # Bot messages in chat_window need to be alligned right hand side

    # parent window
    main_window = Tk()
    main_window.title("Chat Bot v0.1") # window name
    main_window.geometry("400x500+100+100") # dimensions + Location; Width x Height + x + y axis
    main_window.resizable(width=False, height=False) # disable window resize

    # get input function
    def send(input):       
        msg = message_window.get("1.0", END).strip()
        reply = getReply(msg)
        print(f"User: {msg}")
        print(f"Bot: {reply}")
        chat_window.insert(END, f"\nUser: {msg}")
        chat_window.insert(END, f"\nBot: {reply}")

        message_window.delete("1.0", END) # clears message_window after msg is sent


    # main menu bar - possibly delete
    main_menu = Menu(main_window)

    # sub menu - possibly delete
    file_menu = Menu(main_window)
    file_menu.add_command(label="Test 1")
    file_menu.add_command(label="Test 2")
    file_menu.add_command(label="Test 3")

    # main menu widgets - possibly delte
    main_menu.add_cascade(label="Drop Down", menu = file_menu) 
    main_menu.add_command(label="Button 2") 
    main_menu.add_command(label="Button 3") 
    main_window.config(menu=main_menu) 

    # chat window
    chat_window = Text(main_window, bd=1, bg="Grey", width =50, height = 8, cursor="arrow")
    chat_window.place(x=6, y=6, height= 414, width= 370)

    # message window
    message_window = Text(main_window, bg="grey", width=30, cursor="arrow", wrap=WORD)
    message_window.bind("<Return>", send)
    message_window.place(x=6, y=426, height=68, width=300)

    # send button (may not need) (non functional - use "Enter" key)
    enter_button = Button(main_window, text="Enter", bg="grey", activebackground="light grey", width=12, height = 5, command=send)
    enter_button.place(x=312, y=426, height=68, width=82)

    # scrollbar (may not need) (non functional - use scroll wheel)
    scrollbar = Scrollbar(main_window, command=chat_window.yview())
    scrollbar.place(x=375, y=5, height =385)

    return main_window
    #main_window.mainloop()

if __name__=="__main__":
    window = create_window(lambda x: "Placeholder reply funtion")
    window.mainloop()