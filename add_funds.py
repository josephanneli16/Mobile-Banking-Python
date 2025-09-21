from database import *
import tkinter as tk
from PIL import ImageTk
from tkinter import *
import Frames

#Background color
color = "#ffffff"


def load_funds_frame(root, username, password, users_balance, frame1, frame2, deposit_amount, frame, counter):
    
    #Input Validation
    if type(deposit_amount) == int:
        users_balance += deposit_amount

    else:
        added_funds = deposit_amount.get()
        str(added_funds)
        try:
            added_funds.isnumeric()
            added_funds = int(added_funds)
            users_balance += added_funds
            
        except ValueError:
            print("error")
        
        
    #deposit frame
    add_funds_frame = tk.Frame(root, width=500, height=600, bg = color)
    add_funds_frame.grid(row=0, column=0)
    Frames.clear_widgets(frame)
    add_funds_frame.tkraise()
    add_funds_frame.pack_propagate(False)

    #bank logo
    logo_img = ImageTk.PhotoImage(file="assets/chase_logo.png")
    logo_widget = tk.Label(add_funds_frame, image=logo_img, bg = color)
    logo_widget.image = logo_img
    logo_widget.pack()

    #info text
    tk.Label(add_funds_frame, text = "Deposit Successful!", bg = color, fg="black", font=("TkMenuFont", 20)).place(x = 128, y = 150)
    tk.Label(add_funds_frame, text = "Your balance is now:", bg = color, fg="black", font=("TkMenuFont", 20)).place(x = 123, y = 250)
    tk.Label(add_funds_frame, text = "$", bg = color, fg="red", font=("TkMenuFont", 20)).place(x = 195, y = 300)
    tk.Label(add_funds_frame, text = users_balance, bg = color, fg="red", font=("TkMenuFont", 20)).place(x = 220, y = 300)

    #back Button
    back_button = tk.Button(add_funds_frame, text="Back", font=("TkMenuFont", 14),
    bg = color, fg = "black", cursor = "hand2", 
    activebackground="#ababab", command = lambda:Frames.load_frame2(root, frame1, frame2, username, password, users_balance, counter))
    back_button.place(x=380, y=470)


