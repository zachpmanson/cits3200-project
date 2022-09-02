
from logging import root
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

password = "computer"

def create_window(getReply):

    # function to call frame swapping
    def show_frame(frame):
        frame.tkraise()

    # send message function for frame2
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

    # password and gmail authentication - gmail authentication needs work
    def pass_check():
        gmail = "test"
        password = "computer"
        if pass_txt.get()==password and email_txt.get()==gmail:
            print("Logged in!")
            pass_txt.delete(0, 'end')
            email_txt.delete(0, 'end')
            show_frame(frame2)
        else:
            print("Invalid password or gmail")

    def hush():
        print("Bot is now hushed")


    #================== Creating Root Window =================================================#    
    root_window = tk.Tk()
    root_window.title("Chat Bot v0.2") # window name
    root_window.geometry("400x500+1400+400") # dimensions + Location; Width x Height + x + y axis
    root_window.resizable(width=False, height=False) # disable window resize
    root_window.rowconfigure(0, weight=1) # configuring window rows
    root_window.columnconfigure(0, weight=1) # configuring window columns

    # creating login frame1 & chatbot frame2
    frame1 = tk.Frame(root_window)
    frame2 = tk.Frame(root_window)

    # cycling the frames 
    for frame in (frame1, frame2):
        frame.grid(row=0,column=0,sticky='nsew')
        
    #================== Frame 1 - Login/Avatar creation code ======================================================#

    # Background lbl
    bg_lbl = tk.Label(frame1,bg='#333332')
    bg_lbl.place(x=6, y=6,height= 488, width= 388)

    # Inserting test avatar image
    # img = 'chatbot\\images\\tes_image_2.png'
    # img1 = p.Image.open(img)
    # photo = ptk.PhotoImage(img1)
    #image_lbl = tk.Label(frame1, image=photo)
    #image_lbl.place(x=163, y=12, relwidth=0.3, relheight=0.3)

    # Submition button
    submit_btn = tk.Button(frame1, text='Submit',command= pass_check) 
    submit_btn.place(x=163, y=438, height=50, width=75)
    frame1.bind('<Return>', pass_check)

    # Email field
    email_txt = tk.Entry(frame1, bg="#333332", cursor="arrow")
    email_txt.place(x=100, y=373, height=18, width=200)
    email_lbl = tk.Label(frame1, text= "Gmail: ",bg='#333332')
    email_lbl.place(x=100, y=359, height=14)

    # Passowrd field
    pass_txt = tk.Entry(frame1, bg="#333332", cursor="arrow", show= '*')
    pass_txt.place(x=100, y=409, height=18, width=200)
    pass_lbl = tk.Label(frame1, text= "Password: ",bg='#333332')
    pass_lbl.place(x=100, y=395, height=14)

    # Random avatar button
    rand_btn = tk.Button(frame1, text="Randomise!", bg='white')
    rand_btn.place(x=163, y=244, height=50, width=75)

    # Skin buttons & label
    skin_lbl = tk.Label(frame1, text="Skin", bg='white')
    skin_lbl.place(x=50, y=300, height=40, width=75)
    skin_right_btn = tk.Button(frame1)
    skin_right_btn.place(x=131, y=320, height=10, width=20)
    skin_left_btn = tk.Button(frame1)
    skin_left_btn.place(x=24, y=320, height=10, width=20)

    # Eyes buttons & label
    eyes_lbl = tk.Label(frame1, text="Eyes", bg='white')
    eyes_lbl.place(x=50, y=244, height=40, width=75)
    eyes_right_btn = tk.Button(frame1)
    eyes_right_btn.place(x=131, y=264, height=10, width=20)
    eyes_left_btn = tk.Button(frame1)
    eyes_left_btn.place(x=24, y=264, height=10, width=20)

    # Hair buttons & label
    hair_lbl = tk.Label(frame1, text="Hair", bg='white')
    hair_lbl.place(x=50, y=188, height=40, width=75)
    hair_right_btn = tk.Button(frame1)
    hair_right_btn.place(x=131, y=208, height=10, width=20)
    hair_left_btn = tk.Button(frame1)
    hair_left_btn.place(x=24, y=208, height=10, width=20)

    # Mouth buttons & label
    mouth_lbl = tk.Label(frame1, text="Mouth", bg='white')
    mouth_lbl.place(x=275, y=188, height=40, width=75)
    mouth_right_btn = tk.Button(frame1)
    mouth_right_btn.place(x=249, y=208, height=10, width=20)
    mouth_left_btn = tk.Button(frame1)
    mouth_left_btn.place(x=356, y=208, height=10, width=20)

    # Accessories buttons & label
    acc_lbl = tk.Label(frame1, text="Accessories", bg='white')
    acc_lbl.place(x=275, y=244, height=40, width=75)
    acc_right_btn = tk.Button(frame1)
    acc_right_btn.place(x=249, y=264, height=10, width=20)
    acc_left_btn = tk.Button(frame1)
    acc_left_btn.place(x=356, y=264, height=10, width=20)

    # Shirt buttons & label
    shirt_lbl = tk.Label(frame1, text="Shirt", bg='white')
    shirt_lbl.place(x=275, y=300, height=40, width=75)
    shirt_right_btn = tk.Button(frame1)
    shirt_right_btn.place(x=249, y=320, height=10, width=20)
    shirt_left_btn = tk.Button(frame1)
    shirt_left_btn.place(x=357, y=320, height=10, width=20)



    #================== Frame 2 - Chat bot UI code =================================================#
    # chat window
    chat_window = Text(frame2, bd=1, bg="#333332", width =50, height = 8, cursor="arrow", wrap=WORD)
    chat_window.place(x=6, y=6, height= 414, width= 388)
    chat_window.configure(state="disabled") # disables users for inputting directly into window

    # message window
    message_window = Text(frame2, bg="#333332", width=30, cursor="arrow", wrap=WORD)
    message_window.bind('<Return>', send)
    message_window.place(x=6, y=426, height=68, width=388)


    #================== Window button code =========================================================#
    # main menu bar 
    main_menu = Menu(root_window)

    # sub/dropdown menu - is this needed? unsure 
    file_menu = Menu(root_window)
    file_menu.add_command(label="Test 1")
    file_menu.add_command(label="Test 2")
    file_menu.add_command(label="Test 3")

    # main menu widgets 
    main_menu.add_cascade(label="Drop Down", menu = file_menu)  # shows drop down button
    main_menu.add_command(label="Log Out",command=lambda:show_frame(frame1))  # calls return frame1 function
    main_menu.add_command(label="Hush Mode", command=lambda:hush()) # non functional
    root_window.config(menu=main_menu) 

    show_frame(frame1)

    return root_window

if __name__=="__main__":
    window = create_window(lambda x: "Placeholder reply funtion")
    window.mainloop()