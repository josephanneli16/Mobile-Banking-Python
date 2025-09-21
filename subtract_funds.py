from database import *
import tkinter as tk
from PIL import ImageTk
from tkinter import *
import Frames


color = "#ffffff"

"-----------------------------------------------------------"

def load_subtract_frame(root, username, password, balance, frame1, frame2, withdrawal_amount, frame, counter):
    
    if type(withdrawal_amount) == int:
        balance -= withdrawal_amount

    else:
        withdrawal_amount = withdrawal_amount.get()
        withdrawal_amount = int(withdrawal_amount)
        balance -= withdrawal_amount

    #deposit frame
    subtract_funds_frame = tk.Frame(root, width=500, height=600, bg = color)
    subtract_funds_frame.grid(row=0, column=0)
    Frames.clear_widgets(frame)
    subtract_funds_frame.tkraise()
    subtract_funds_frame.pack_propagate(False)

    #bank logo
    logo_img = ImageTk.PhotoImage(file="assets/chase_logo.png")
    logo_widget = tk.Label(subtract_funds_frame, image=logo_img, bg = color)
    logo_widget.image = logo_img
    logo_widget.pack()

    #info text
    tk.Label(subtract_funds_frame, text = "Withdrawal Successful!", bg = color, fg="black", font=("TkMenuFont", 20)).place(x = 105, y = 150)
    tk.Label(subtract_funds_frame, text = "Your balance is now:", bg = color, fg="black", font=("TkMenuFont", 20)).place(x = 123, y = 250)
    tk.Label(subtract_funds_frame, text = "$", bg = color, fg="red", font=("TkMenuFont", 20)).place(x = 195, y = 300)
    tk.Label(subtract_funds_frame, text = balance, bg = color, fg="red", font=("TkMenuFont", 20)).place(x = 220, y = 300)

    if balance < 0:
        tk.Label(subtract_funds_frame, text = "You Owe Money To The Bank Now!", bg = color, fg="black", font=("TkMenuFont", 16)).place(x = 85, y = 400)

    #tk.label(subtract_funds_frame, text = "Withdrawal Successful!", bg = color, fg="black", font=("TkMenuFont", 20)).place(x = 128, y = 150)

    #back Button
    back_button = tk.Button(subtract_funds_frame, text="Back", font=("TkMenuFont", 14),
    bg = color, fg = "black", cursor = "hand2", 
    activebackground="#ababab", command = lambda:Frames.load_frame2(root, frame1, frame2, username, password, balance, counter))
    back_button.place(x=380, y=470)