from database import *
import tkinter as tk
from PIL import ImageTk
from tkinter import *
import Frames
import check_pin

#Window color
color = "#ffffff"

def load_pin_frame(root, username, password, frame2, frame1, users_balance, counter):

    #Window structure
    pin_frame = tk.Frame(root, width=500, height=600, bg = color)
    pin_frame.grid(row=0, column=0)
    
    Frames.clear_widgets(frame2)
    pin_frame.tkraise()
    pin_frame.pack_propagate(False)

    #bank logo
    logo_img = ImageTk.PhotoImage(file="assets/chase_logo.png")
    logo_widget = tk.Label(pin_frame, image=logo_img, bg = color)
    logo_widget.image = logo_img
    logo_widget.pack()

    #User ID Text
    tk.Label(pin_frame, text = "User ID:", bg = color, fg="black", font=("TkMenuFont", 17)).place(x = 50, y = 150)
    entered_username = tk.Entry(pin_frame, bg = color, fg="black", font=("TkMenuFont", 17))
    entered_username.place(x = 160, y = 150, width=170, height=35)

    #Old Pin Text
    tk.Label(pin_frame, text = "Old Pin:", bg = color, fg="black", font=("TkMenuFont", 17)).place(x = 50, y = 250)
    old_pin = tk.Entry(pin_frame, bg = color, fg="black", font=("TkMenuFont", 17))
    old_pin.place(x = 160, y = 250, width=170, height=35)

    #New Pin Text
    tk.Label(pin_frame, text = "New Pin:", bg = color, fg="black", font=("TkMenuFont", 17)).place(x = 50, y = 350)
    new_pin = tk.Entry(pin_frame, bg = color, fg="black", font=("TkMenuFont", 17))
    new_pin.place(x = 160, y = 350, width=170, height=35)

    #Enter Button
    enter_button = tk.Button(pin_frame, text=" Enter ", font=("TkMenuFont", 14),
    bg = color, fg = "black", cursor = "hand2", 
    activebackground="#ababab", command = lambda:check_pin.check_user_pin(root, frame1, frame2, entered_username, username, password, old_pin, new_pin, pin_frame, users_balance, counter))
    enter_button.place(x=200, y=420)

    #back Button
    back_button = tk.Button(pin_frame, text="Back", font=("TkMenuFont", 14),
    bg = color, fg = "black", cursor = "hand2", 
    activebackground="#ababab", command = lambda:Frames.load_frame2(root, frame1, frame2, username, password, users_balance, counter))
    back_button.place(x=380, y=500)

