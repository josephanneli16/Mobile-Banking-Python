import tkinter as tk
from PIL import ImageTk
from tkinter import *
from input import *
from database import *
from input import take_input
import account_info 
import deposit
import withdrawal
import change_pin
import updating_database
import create_account


color = "#ffffff"


def clear_widgets(frame):
    for widget in frame. winfo_children():
        widget.destroy()


def load_frame1(root, frame1, frame2, users_balance):
    print(users_balance)
    
    clear_widgets(frame2)
    frame1.tkraise()
    frame1.pack_propagate(False)


    #Frame1 logo Widget
    logo_img = ImageTk.PhotoImage(file="assets/chase_logo.png")
    logo_widget = tk.Label(frame1, image=logo_img, bg = color)
    logo_widget.image = logo_img
    logo_widget.pack()


    #Label for USER ID and Password on frame 1
    tk.Label(frame1, text = "User ID", bg = color, fg="black", font=("TkMenuFont", 15)).place(x = 48, y = 183)
    username = tk.Entry(frame1,bg = color, fg="black", font=("TkMenuFont", 15))
    username.place(x = 150, y = 180, width=200, height=35)
    
    tk.Label(frame1, text = "PIN", bg = color, fg="black", font=("TkMenuFont", 15)).place(x = 65, y = 252)
    password = tk.Entry(frame1, bg = color, fg="black", font=("TkMenuFont", 15))
    password.place(x = 150, y = 250, width=200, height=35)

    
    #Button for Login in frame 1
    tk.Button(frame1, text="Login", font=("TkMenuFont", 16),
    bg = color, fg = "black", cursor = "hand2", 
    activebackground="#ababab", 
    command = lambda:take_input(root, username, password, credentials, passwords, frame1, frame2, color)
    ).place(x = 212, y = 330)

    #Button for new account in frame 1
    tk.Button(frame1, text="Create Account", font=("TkMenuFont", 15),
    bg = color, fg = "black", cursor = "hand2", 
    activebackground="#ababab", 
    command = lambda:create_account.signup(root, username, password, credentials, passwords, frame1, frame2, color, users_balance)
    ).place(x = 300, y = 500)



#Function to load frame 2
def load_frame2(root, frame1, frame2, username, password, users_balance, counter):
    
    print(users_balance)
    clear_widgets(frame1)
    frame2.tkraise()
    frame2.pack_propagate(False)

    #logo Widget
    logo_img = ImageTk.PhotoImage(file="assets/chase_logo.png")
    logo_widget = tk.Label(frame2, image=logo_img, bg = color)
    logo_widget.image = logo_img
    logo_widget.pack(pady = 20)

    #Buttons
    account_button = tk.Button(frame2, text="Account", font=("TkMenuFont", 16),
    bg = color, fg = "black", cursor = "hand2", 
    activebackground="#ababab", command = lambda:account_info.load_frame_account(root, username, password, users_balance, frame2, frame1, counter))
    account_button.place(x=120, y=200)

    deposit_button = tk.Button(frame2, text="Deposit", font=("TkMenuFont", 16),
    bg = color, fg = "black", cursor = "hand2", 
    activebackground="#ababab", command = lambda:deposit.load_deposit_frame(root, username, password, users_balance, frame2, frame1, counter))
    deposit_button.place(x=122, y=300)

    transfer_button = tk.Button(frame2, text="Transfer", font=("TkMenuFont", 16),
    bg = color, fg = "black", cursor = "hand2", 
    activebackground="#ababab")
    transfer_button.place(x=116, y=400)

    withdrawal_button = tk.Button(frame2, text="Withdrawal", font=("TkMenuFont", 16),
    bg = color, fg = "black", cursor = "hand2", 
    activebackground="#ababab", command = lambda:withdrawal.load_withdrawal_frame(root, username, password, users_balance, frame2, frame1, counter))
    withdrawal_button.place(x=275, y=300)

    change_button = tk.Button(frame2, text="PIN Change", font=("TkMenuFont", 16),
    bg = color, fg = "black", cursor = "hand2", 
    activebackground="#ababab", command = lambda:change_pin.load_pin_frame(root, username, password, frame2, frame1, users_balance, counter))
    change_button.place(x=275, y=200)

    exit_button = tk.Button(frame2, text="   Logout   ", font=("TkMenuFont", 16),
    bg = color, fg = "black", cursor = "hand2", 
    activebackground="#ababab", command=lambda:updating_database.update_database(root, frame1, frame2, username, password, users_balance, counter))
    exit_button.place(x=275, y=400)








#admin