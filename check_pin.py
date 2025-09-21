from database import *
import tkinter as tk
from PIL import ImageTk
from tkinter import *
import Frames

#Background Color
color = "#ffffff"

def check_user_pin(root, frame1, frame2, entered_username, username, password, old_pin, new_pin, pin_frame, users_balance, counter):

    entered_username = entered_username.get()
    old_pin = old_pin.get()
    new_pin = new_pin.get()

    print(username, password)
    print(entered_username, old_pin, new_pin)

    if entered_username == username:
        if old_pin == password:
            tk.Label(pin_frame, text = "    Pin Successfully Changed!    ", bg = color, fg="red", font=("TkMenuFont", 15)).place(x = 105, y = 470)
            passwords[counter] = new_pin
            
    if entered_username != username or old_pin != password:
        tk.Label(pin_frame, text = "  Username or Old Pin Incorrect!  ", bg = color, fg="red", font=("TkMenuFont", 15)).place(x = 95, y = 470)
    
    print(password)
    
    #Back Button
    back_button = tk.Button(pin_frame, text="Back", font=("TkMenuFont", 14),
    bg = color, fg = "black", cursor = "hand2", 
    activebackground="#ababab", command = lambda:Frames.load_frame2(root, frame1, frame2, username, password, users_balance, counter))
    back_button.place(x=380, y=500)

    

