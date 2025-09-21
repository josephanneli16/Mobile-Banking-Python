from database import *
import tkinter as tk
from PIL import ImageTk
from tkinter import *
import Frames

def signup(root, username, password, credentials, passwords, frame1, frame2, color, users_balance):
    
    #Sig up Frame
    signup_frame = tk.Frame(root, width=500, height=600, bg = color)
    signup_frame.grid(row=0, column=0)
    
    Frames.clear_widgets(frame1)
    signup_frame.tkraise()
    signup_frame.pack_propagate(False)

    #bank logo
    logo_img = ImageTk.PhotoImage(file="assets/chase_logo.png")
    logo_widget = tk.Label(signup_frame, image=logo_img, bg = color)
    logo_widget.image = logo_img
    logo_widget.pack()

    #Sign up text
    tk.Label(signup_frame, text = "Sign Up", bg = color, fg="black", font=("TkMenuFont", 16)).place(x = 210, y = 130)

    #Label for USER ID and Pin for sign up
    tk.Label(signup_frame, text = "User ID", bg = color, fg="black", font=("TkMenuFont", 15)).place(x = 48, y = 183)
    new_username = tk.Entry(signup_frame,bg = color, fg="black", font=("TkMenuFont", 15))
    new_username.place(x = 150, y = 180, width=200, height=35)
    
    tk.Label(signup_frame, text = "PIN", bg = color, fg="black", font=("TkMenuFont", 15)).place(x = 65, y = 252)
    new_password = tk.Entry(signup_frame, bg = color, fg="black", font=("TkMenuFont", 15))
    new_password.place(x = 150, y = 250, width=200, height=35)

    tk.Button(signup_frame, text="Create", font=("TkMenuFont", 16),
    bg = color, fg = "black", cursor = "hand2", 
    activebackground="#ababab", 
    command = lambda:check_credentials(new_username, new_password, signup_frame, color)
    ).place(x = 205, y = 330)

    #back button
    back_button = tk.Button(signup_frame, text="Back", font=("TkMenuFont", 14),
    bg = color, fg = "black", cursor = "hand2", 
    activebackground="#ababab", command = lambda:Frames.load_frame1(root, frame1, frame2, users_balance))
    back_button.place(x=380, y=470)



def check_credentials(new_username, new_password, signup_frame, color):
    money = 0
    new_username = new_username.get()
    new_password = new_password.get()

    #Checking for users input
    if new_username in credentials:
        print("username exist")
        tk.Label(signup_frame, text = "   Username Already Exist!   ", bg = color, fg="black", font=("TkMenuFont", 16)).place(x = 120, y = 400)
    
    else:
        if len(new_username) < 6:
            tk.Label(signup_frame, text = "Enter 6 or More Characters!", bg = color, fg="black", font=("TkMenuFont", 16)).place(x = 115, y = 400)

        else:
            if new_password.isnumeric():
                if len(new_password) < 6:
                    tk.Label(signup_frame, text = "    Enter 6 or More Digits    ", bg = color, fg="black", font=("TkMenuFont", 16)).place(x = 120, y = 400)

                else:
                    tk.Label(signup_frame, text = "        Account Created!        ", bg = color, fg="black", font=("TkMenuFont", 16)).place(x = 120, y = 400)
                    credentials.append(new_username)
                    passwords.append(new_password)
                    balance.append(money)
                    print(credentials)
                    print(passwords)
                    print(balance)
                    
            else:
                tk.Label(signup_frame, text = "       Enter Digits for PIN       ", bg = color, fg="black", font=("TkMenuFont", 16)).place(x = 112, y = 400)
