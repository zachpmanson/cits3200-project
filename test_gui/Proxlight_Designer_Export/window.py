from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import os
print("Working dir:", os.getcwd())

def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("400x550")
window.configure(bg = "#4f415a")
canvas = Canvas(
    window,
    bg = "#4f415a",
    height = 550,
    width = 400,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

img0 = Image.open("img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 138, y = 439,
    width = 106,
    height = 43)

img1 = PhotoImage(file = f"C:\\Users\\zarhm\\Documents\\GitHub\\cits3200-project\\test_gui\\Proxlight_Designer_Export\\img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 138, y = 495,
    width = 106,
    height = 43)

img2 = PhotoImage(file = f"C:\\Users\\zarhm\\Documents\\GitHub\\cits3200-project\\test_gui\\Proxlight_Designer_Export\\img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 157, y = 388,
    width = 34,
    height = 33)

img3 = PhotoImage(file = f"C:\\Users\\zarhm\\Documents\\GitHub\\cits3200-project\\test_gui\\Proxlight_Designer_Export\\img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b3.place(
    x = 195, y = 388,
    width = 34,
    height = 33)

img4 = PhotoImage(file = f"C:\\Users\\zarhm\\Documents\\GitHub\\cits3200-project\\test_gui\\Proxlight_Designer_Export\\img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b4.place(
    x = 10, y = 388,
    width = 34,
    height = 33)

img5 = PhotoImage(file = f"C:\\Users\\zarhm\\Documents\\GitHub\\cits3200-project\\test_gui\\Proxlight_Designer_Export\\img5.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b5.place(
    x = 10, y = 259,
    width = 34,
    height = 33)

img6 = PhotoImage(file = f"C:\\Users\\zarhm\\Documents\\GitHub\\cits3200-project\\test_gui\\Proxlight_Designer_Export\\img6.png")
b6 = Button(
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b6.place(
    x = 10, y = 327,
    width = 34,
    height = 33)

img7 = PhotoImage(file = f"C:\\Users\\zarhm\\Documents\\GitHub\\cits3200-project\\test_gui\\Proxlight_Designer_Export\\img7.png")
b7 = Button(
    image = img7,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b7.place(
    x = 195, y = 259,
    width = 34,
    height = 33)

img8 = PhotoImage(file = f"C:\\Users\\zarhm\\Documents\\GitHub\\cits3200-project\\test_gui\\Proxlight_Designer_Export\\img8.png")
b8 = Button(
    image = img8,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b8.place(
    x = 195, y = 327,
    width = 34,
    height = 33)

img9 = PhotoImage(file = f"C:\\Users\\zarhm\\Documents\\GitHub\\cits3200-project\\test_gui\\Proxlight_Designer_Export\\img9.png")
b9 = Button(
    image = img9,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b9.place(
    x = 157, y = 259,
    width = 34,
    height = 33)

img10 = PhotoImage(file = f"C:\\Users\\zarhm\\Documents\\GitHub\\cits3200-project\\test_gui\\Proxlight_Designer_Export\\img10.png")
b10 = Button(
    image = img10,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b10.place(
    x = 342, y = 388,
    width = 34,
    height = 33)

img11 = PhotoImage(file = f"C:\\Users\\zarhm\\Documents\\GitHub\\cits3200-project\\test_gui\\Proxlight_Designer_Export\\img11.png")
b11 = Button(
    image = img11,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b11.place(
    x = 342, y = 259,
    width = 34,
    height = 33)

img12 = PhotoImage(file = f"C:\\Users\\zarhm\\Documents\\GitHub\\cits3200-project\\test_gui\\Proxlight_Designer_Export\\img12.png")
b12 = Button(
    image = img12,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b12.place(
    x = 342, y = 327,
    width = 34,
    height = 33)

img13 = PhotoImage(file = f"C:\\Users\\zarhm\\Documents\\GitHub\\cits3200-project\\test_gui\\Proxlight_Designer_Export\\img13.png")
b13 = Button(
    image = img13,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b13.place(
    x = 157, y = 327,
    width = 34,
    height = 33)

window.resizable(False, False)
window.mainloop()
