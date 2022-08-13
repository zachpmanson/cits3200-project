import interface 
import handle_msg
# import chatbot 
# import handle_msg 

if __name__=="__main__":
    window = interface.create_window(handle_msg.getReply)
    window.mainloop()