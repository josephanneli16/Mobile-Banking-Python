from database import *
import tkinter as tk
from PIL import ImageTk
from tkinter import *
import Frames


color = "#ffffff"

def load_frame_account(root, username, password, users_balance, frame2, frame1, counter):
   
    #Window title
    root.title("ATM Software")
    
    #Window structure
    frame_account = tk.Frame(root, width=500, height=600, bg = color)
    frame_account.grid(row=0, column=0)
    print(username, password, users_balance)
    Frames.clear_widgets(frame2)
    frame_account.tkraise()
    frame_account.pack_propagate(False)


    #Frame account_info logo Widget
    logo_img = ImageTk.PhotoImage(file="assets/chase_logo.png")
    logo_widget = tk.Label(frame_account, image=logo_img, bg = color)
    logo_widget.image = logo_img
    logo_widget.pack(pady = 20)

    #Text User ID
    tk.Label(frame_account, text = "User ID:", bg = color, fg="black", font=("TkMenuFont", 16)).place(x = 120, y = 200, anchor=CENTER)
    tk.Label(frame_account, text = username, bg = color, fg="red", font=("TkMenuFont", 16)).place(x = 120, y = 260, anchor=CENTER)

    #Text Password
    tk.Label(frame_account, text = "Pin Number:", bg = color, fg="black", font=("TkMenuFont", 16)).place(x = 365, y = 200, anchor=CENTER)
    tk.Label(frame_account, text = password, bg = color, fg="red", font=("TkMenuFont", 16)).place(x = 365, y = 260, anchor=CENTER)

    #Text Balance
    tk.Label(frame_account, text = "Balance:", bg = color, fg="black", font=("TkMenuFont", 16)).place(x = 245, y = 350, anchor=CENTER)
    tk.Label(frame_account, text = "$", bg = color, fg="red", font=("TkMenuFont", 16)).place(x = 210, y = 380)
    tk.Label(frame_account, text = users_balance, bg = color, fg="red", font=("TkMenuFont", 16)).place(x = 225, y = 380)

    #If users balance is below 0
    if users_balance < 0:
         tk.Label(frame_account, text = "Don't Forget to Pay Your Debt!", bg = color, fg="black", font=("TkMenuFont", 16)).place(x = 100, y = 450)

    #back button
    back_button = tk.Button(frame_account, text="Back", font=("TkMenuFont", 15),
    bg = color, fg = "black", cursor = "hand2", 
    activebackground="#ababab", command = lambda:Frames.load_frame2(root, frame1, frame2, username, password, users_balance, counter))
    back_button.place(x=380, y=510)



