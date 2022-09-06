
from tkinter import *
import tkinter as tk
from itertools import cycle
from PIL import ImageTk, Image
import python_avatars as pa
import time 
import cairosvg

# outstanding UI issues
# chat_window text formating, user and bot responses
# returning user cursor in message_window to correct position
# figuring out hush function requirements
# custom buttons, gui colour scheme
# implement avatars to customisation buttons
# check ios - buttons
# binding return key to submit button
# bot binds return key after visiting frame2 to frame1

set_font = ("Roboto", 11) # setting font style and size

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
            # time.sleep(1) test code
            #chat_window.tag_configure("right", justify='right') # configures window to input text right alligned
            #chat_window.tag_add("right", 1.0, "end")
            chat_window.insert(END, f"\nBot: {reply}")
            chat_window.configure(state="disabled") # disables users for inputting directly into window
            
            message_window.delete("1.0", END) # clears message_window after msg is sent

    
    def hush(): 
        print("Bot is now hushed")
        root_window.wm_state('iconic')
        # ime.sleep(10)
        

    def focus_window(): # import to open window
        root_window.wm_state('normal')

    #================== Creating Root Window =================================================#    
    root_window = tk.Tk()
    root_window.title("Chat Bot v0.2") # window name
    root_window.geometry("400x500+1400+400") # dimensions + Location; Width x Height + x + y axis
    root_window.resizable(width=False, height=False) # disable window resize
    root_window.rowconfigure(0, weight=1) # configuring window rows
    root_window.columnconfigure(0, weight=1) # configuring window columns

    # creating login frame1 & chatbot frame2
    frame1 = tk.Frame(root_window, bg= '#FFFFFF') #4F415A
    frame2 = tk.Frame(root_window, bg= '#FFFFFF') #3E4971

    # cycling the frames 
    for frame in (frame1, frame2):
        frame.grid(row=0,column=0,sticky='nsew')
        
    #================== Frame 1 - Login/Avatar creation code ======================================================#

    # Background lbl
    bg_lbl = tk.Label(frame1,bg='#84CBEE')
    bg_lbl.place(x=6, y=6,height= 488, width= 388)

    # Inserting test avatar image
    av_bdr =tk.Frame(frame1, highlightbackground = "black", highlightthickness = 2, bd=0) # creating avatar border
    av_bdr.place(x=124, y=19, height=202, width=152)
    photo = Image.open('my_avatar.png') # importing the image
    resize_img = photo.resize((200, 200), Image.LANCZOS) # resizing 
    img = ImageTk.PhotoImage(resize_img)
    av_lbl = tk.Label(frame1) # creating image label
    av_lbl.image =img # saving reference of photo 
    av_lbl.place(x=125, y=20, height=200, width=150) # placing the image label
    av_lbl.configure(image=img) # setting the label to the image

    # Submition button
    submit_btn = tk.Button(frame1, text='Submit',command=lambda:show_frame(frame2)) 
    submit_btn.place(x=163, y=438, height=30, width=75)
    submit_btn.bind('<Return>', show_frame)
    # submit_btn.focus()
    
    # Random avatar button
    rand_btn = tk.Button(frame1, text="Randomise!", bg='white')    
    rand_btn.place(x=163, y=300, height=50, width=75)

    list_skin_color = cycle(['TANNED','YELLOW','PALE','LIGHT','BROWN','DARK_BROWN','BLACK'])
    list_eye_type = cycle(['CLOSED', 'CRY', 'DEFAULT', 'EYE_ROLL', 'HAPPY', 'HEART', 'SIDE', 'SQUINT', 'SURPRISED', 'WINK_WACKY', 'WINK', 'X_DIZZY'])
    list_top_type = cycle(['NONE', 'BIG_HAIR', 'BOB', 'BUN', 'CURLY', 'CURVY', 'DREADS', 'FRIDA', 'FRIZZLE', 'FRO_BAND', 'FRO', 'LONG_NOT_TOO_LONG', 'SHAGGY_MULLET', 'SHAGGY', 'SHAVED_SIDES', 'SHORT_CURLY', 'SHORT_DREADS_1', 'SHORT_DREADS_2', 'SHORT_FLAT', 'SHORT_ROUND', 'SHORT_WAVED', 'SIDES', 'STRAIGHT_1', 'STRAIGHT_2', 'STRAIGHT_STRAND'])
    list_mouth_type = cycle(['DEFAULT','CONCERNED','DISBELIEF','EATING','GRIMACE','SAD','SCREAM_OPEN','SERIOUS','SMILE','TONGUE','TWINKLE','VOMIT'])
    list_accessories_type = cycle(['NONE', 'KURT','ROUND','SUNGLASSES','WAYFARERS'])
    list_clothe_type = cycle(['BLAZER_SHIRT','BLAZER_SWEATER','COLLAR_SWEATER','GRAPHIC_SHIRT','HOODIE','OVERALL','SHIRT_CREW_NECK','SHIRT_SCOOP_NECK','SHIRT_V_NECK'])

    list_skin_colors = ['TANNED','YELLOW','PALE','LIGHT','BROWN','DARK_BROWN','BLACK']
    list_eye_types = ['CLOSED', 'CRY', 'DEFAULT', 'EYE_ROLL', 'HAPPY', 'HEART', 'SIDE', 'SQUINT', 'SURPRISED', 'WINK_WACKY', 'WINK', 'X_DIZZY']
    list_top_types = ['NONE', 'BIG_HAIR', 'BOB', 'BUN', 'CURLY', 'CURVY', 'DREADS', 'FRIDA', 'FRIZZLE', 'FRO_BAND', 'FRO', 'LONG_NOT_TOO_LONG', 'SHAGGY_MULLET', 'SHAGGY', 'SHAVED_SIDES', 'SHORT_CURLY', 'SHORT_DREADS_1', 'SHORT_DREADS_2', 'SHORT_FLAT', 'SHORT_ROUND', 'SHORT_WAVED', 'SIDES', 'STRAIGHT_1', 'STRAIGHT_2', 'STRAIGHT_STRAND']
    list_mouth_types = ['DEFAULT','CONCERNED','DISBELIEF','EATING','GRIMACE','SAD','SCREAM_OPEN','SERIOUS','SMILE','TONGUE','TWINKLE','VOMIT']
    list_accessories_types = ['NONE', 'KURT','ROUND','SUNGLASSES','WAYFARERS']
    list_clothe_types = ['BLAZER_SHIRT','BLAZER_SWEATER','COLLAR_SWEATER','GRAPHIC_SHIRT','HOODIE','OVERALL','SHIRT_CREW_NECK','SHIRT_SCOOP_NECK','SHIRT_V_NECK']
    
    def change_skin(sk=0, ey=0, ha=0, mo=0, ac=0, sh=0):
        skin = 'TANNED'
        eyes = 'DEFAULT'
        hair = 'NONE'
        mouth = 'DEFAULT'
        accessories = 'DEFAULT'
        clothes = 'BLAZER_SHIRT'
        
        #Skin
        if sk == 1:
            skin = next(list_skin_color)
        if sk == -1:
            for i in range(len(list_skin_colors)-1):
                skin = next(list_skin_color)
        if sk == 0:
            for i in range(len(list_skin_colors)):
                skin = next(list_skin_color)

        #Eyes
        if ey == 1:
            eyes = next(list_eye_type)
        if ey == -1:
            for i in range(len(list_eye_types)-1):
                eyes = next(list_eye_type)
        if ey == 0:
            for i in range(len(list_eye_types)):
                eyes = next(list_eye_type)
        
        #Hair
        if ha == 1:
            hair = next(list_top_type)
        if ha == -1:
            for i in range(len(list_top_types)-1):
                hair = next(list_top_type)
        if ha == 0:
            for i in range(len(list_top_types)):
                hair = next(list_top_type)
        
        #Mouth
        if mo == 1:
            mouth = next(list_mouth_type)
        if mo == -1:
            for i in range(len(list_mouth_types)-1):
                mouth = next(list_mouth_type)
        if mo == 0:
            for i in range(len(list_mouth_types)):
                mouth = next(list_mouth_type)
        
        #Accessories
        if ac == 1:
            accessories = next(list_accessories_type)
        if ac == -1:
            for i in range(len(list_accessories_types)-1):
                accessories = next(list_accessories_type)
        if ac == 0:
            for i in range(len(list_accessories_types)):
                accessories = next(list_accessories_type)
        
        #Clothes
        if sh == 1:
            clothes = next(list_clothe_type)
        if sh == -1:
            for i in range(len(list_clothe_types)-1):
                clothes = next(list_clothe_type)
        if sh == 0:
            for i in range(len(list_clothe_types)):
                clothes = next(list_clothe_type)
        
        my_avatar = pa.Avatar(
            skin_color=eval('pa.SkinColor.%s' % skin),
            eyes=eval('pa.EyeType.%s' % eyes),
            top=eval('pa.HairType.%s' % hair),
            mouth=eval('pa.MouthType.%s' % mouth),
            accessory=eval('pa.AccessoryType.%s' % accessories),
            clothing=eval('pa.ClothingType.%s' % clothes),
        )
        my_avatar.render("my_avatar.svg")
        cairosvg.svg2png(url="my_avatar.svg", write_to="my_avatar.png")
    


    # Skin buttons & label
    skin_bdr =tk.Frame(frame1, highlightbackground = "black", highlightthickness = 2, bd=0) # creating background border
    skin_bdr.place(x=49, y=349, height=42, width=77) # placing border
    skin_lbl = tk.Label(frame1, text="Skin", bg='white') # creating skin label
    skin_lbl.place(x=50, y=350, height=40, width=75) # placing skin label
    skin_right_btn = tk.Button(frame1, command= lambda: change_skin(1, 0, 0, 0, 0, 0)) # creating right button
    skin_right_btn.place(x=131, y=370, height=10, width=20) # placing right button
    skin_left_btn = tk.Button(frame1, command= lambda: change_skin(-1, 0, 0, 0, 0, 0)) # creating left button
    skin_left_btn.place(x=24, y=370, height=10, width=20) # placing right button

    # Eyes buttons & label
    eyes_bdr =tk.Frame(frame1, highlightbackground = "black", highlightthickness = 2, bd=0)
    eyes_bdr.place(x=49, y=293, height=42, width=77)
    eyes_lbl = tk.Label(frame1, text="Eyes", bg='white')
    eyes_lbl.place(x=50, y=294, height=40, width=75)
    eyes_right_btn = tk.Button(frame1, command= lambda: change_skin(0, 1, 0, 0, 0, 0))
    eyes_right_btn.place(x=131, y=314, height=10, width=20)
    eyes_left_btn = tk.Button(frame1, command= lambda: change_skin(0, -1, 0, 0, 0, 0))
    eyes_left_btn.place(x=24, y=314, height=10, width=20)

    # Hair buttons & label
    hair_bdr =tk.Frame(frame1, highlightbackground = "black", highlightthickness = 2, bd=0)
    hair_bdr.place(x=49, y=237, height=42, width=77)
    hair_lbl = tk.Label(frame1, text="Hair", bg='white')
    hair_lbl.place(x=50, y=238, height=40, width=75)
    hair_right_btn = tk.Button(frame1, command= lambda: change_skin(0, 0, 1, 0, 0, 0))
    hair_right_btn.place(x=131, y=258, height=10, width=20)
    hair_left_btn = tk.Button(frame1, command= lambda: change_skin(0, 0, -1, 0, 0, 0))
    hair_left_btn.place(x=24, y=258, height=10, width=20)


    # Mouth buttons & label
    mouth_bdr =tk.Frame(frame1, highlightbackground = "black", highlightthickness = 2, bd=0)
    mouth_bdr.place(x=274, y=349, height=42, width=77)
    mouth_lbl = tk.Label(frame1, text="Mouth", bg='white')
    mouth_lbl.place(x=275, y=350, height=40, width=75)
    mouth_right_btn = tk.Button(frame1, command= lambda: change_skin(0, 0, 0, 1, 0, 0))
    mouth_right_btn.place(x=249, y=370, height=10, width=20)
    mouth_left_btn = tk.Button(frame1, command= lambda: change_skin(0, 0, 0, -1, 0, 0))
    mouth_left_btn.place(x=356, y=370, height=10, width=20)

    # Accessories buttons & label
    acc_bdr =tk.Frame(frame1, highlightbackground = "black", highlightthickness = 2, bd=0)
    acc_bdr.place(x=274, y=293, height=42, width=77)
    acc_lbl = tk.Label(frame1, text="Accessories", bg='white')
    acc_lbl.place(x=275, y=294, height=40, width=75)
    acc_right_btn = tk.Button(frame1, command= lambda: change_skin(0, 0, 0, 0, 1, 0))
    acc_right_btn.place(x=249, y=314, height=10, width=20)
    acc_left_btn = tk.Button(frame1, command= lambda: change_skin(0, 0, 0, 0, -1, 0))
    acc_left_btn.place(x=356, y=314, height=10, width=20)

    # Shirt buttons & label
    shirt_bdr =tk.Frame(frame1, highlightbackground = "black", highlightthickness = 2, bd=0)
    shirt_bdr.place(x=274, y=237, height=42, width=77)
    shirt_lbl = tk.Label(frame1, text="Shirt", bg='white')
    shirt_lbl.place(x=275, y=238, height=40, width=75)
    shirt_right_btn = tk.Button(frame1, command= lambda: change_skin(0, 0, 0, 0, 0, 1))
    shirt_right_btn.place(x=249, y=258, height=10, width=20)
    shirt_left_btn = tk.Button(frame1, command= lambda: change_skin(0, 0, 0, 0, 0, -1))
    shirt_left_btn.place(x=357, y=258, height=10, width=20)

    #================== Frame 2 - Chat bot UI code =================================================#
    # chat window
    chat_window = Text(frame2, bd=1, bg="#84CBEE", width =50, height = 8, cursor="arrow", wrap=WORD, font= set_font)
    chat_window.place(x=6, y=6, height= 414, width= 388)
    chat_window.configure(state="disabled") # disables users for inputting directly into window

    # message window
    message_window = Text(frame2, bg="#84CBEE", width=30, cursor="arrow", wrap=WORD, font= set_font)
    message_window.bind('<Return>', send)
    message_window.place(x=6, y=426, height=68, width=388)
    

    #================== Window button code =========================================================#
    # main menu bar 
    main_menu = Menu(root_window)

    # sub/dropdown menu - is this needed? unsure 
    file_menu = Menu(root_window)
    file_menu.add_command(label="Test 1") # un assigned menu
    file_menu.add_command(label="Log Out",command=lambda:show_frame(frame1))  # calls return frame1 function
    file_menu.add_command(label="Hush Mode", command=lambda:hush()) # calls hush function

    # main menu widgets 
    main_menu.add_cascade(label="Options", menu = file_menu)  # shows drop down button
    root_window.config(menu=main_menu) 

    show_frame(frame1)
    
    return root_window

if __name__=="__main__":
    window = create_window(lambda x: "Placeholder reply funtion")
    window.mainloop()