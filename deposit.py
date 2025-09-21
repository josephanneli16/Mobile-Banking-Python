from database import *
import tkinter as tk
from PIL import ImageTk
from tkinter import *
import Frames
import add_funds

color = "#ffffff"

def load_deposit_frame(root, username, password, users_balance, frame2, frame1, counter):

    #deposit frame
    deposit_frame = tk.Frame(root, width=500, height=600, bg = color)
    deposit_frame.grid(row=0, column=0)
    print(username, password, users_balance)
    Frames.clear_widgets(frame2)
    deposit_frame.tkraise()
    deposit_frame.pack_propagate(False)

    #bank logo
    logo_img = ImageTk.PhotoImage(file="assets/chase_logo.png")
    logo_widget = tk.Label(deposit_frame, image=logo_img, bg = color)
    logo_widget.image = logo_img
    logo_widget.pack()

    #quick deposit text
    tk.Label(deposit_frame, text = "Quick Deposit", bg = color, fg="black", font=("TkMenuFont", 17)).place(x = 175, y = 120)

    #quick deposit button
    ten_button = tk.Button(deposit_frame, text=" $ 10 ", font=("TkMenuFont", 17),
    bg = color, fg = "black", cursor = "hand2", 
    activebackground="#ababab", command=lambda:add_funds.load_funds_frame(root, username, password, users_balance, frame1, frame2, 10, deposit_frame, counter))
    ten_button.place(x=160, y=180)

    twenty_button = tk.Button(deposit_frame, text=" $ 20 ", font=("TkMenuFont", 17),
    bg = color, fg = "black", cursor = "hand2", 
    activebackground="#ababab", command=lambda:add_funds.load_funds_frame(root, username, password, users_balance, frame1, frame2, 20, deposit_frame, counter))
    twenty_button.place(x=260, y=180)

    fifty_button = tk.Button(deposit_frame, text=" $ 50 ", font=("TkMenuFont", 17),
    bg = color, fg = "black", cursor = "hand2", 
    activebackground="#ababab", command=lambda:add_funds.load_funds_frame(root, username, password, users_balance, frame1, frame2, 50, deposit_frame, counter))
    fifty_button.place(x=160, y=230)

    hundred_button = tk.Button(deposit_frame, text="$ 100", font=("TkMenuFont", 17),
    bg = color, fg = "black", cursor = "hand2", 
    activebackground="#ababab", command=lambda:add_funds.load_funds_frame(root, username, password, users_balance, frame1, frame2, 100, deposit_frame, counter))
    hundred_button.place(x=260, y=230)

    #Custom deposit text
    tk.Label(deposit_frame, text = "Custom Deposit", bg = color, fg="black", font=("TkMenuFont", 17)).place(x = 165, y = 350)


    #Custom deposit Entry
    tk.Label(deposit_frame, text = "$", bg = color, fg="black", font=("TkMenuFont", 17)).place(x = 105, y = 410)
    custom_deposit = tk.Entry(deposit_frame, bg = color, fg="black", font=("TkMenuFont", 18))
    custom_deposit.place(x = 165, y = 410, width=170, height=35)


    #Enter Button
    enter_button = tk.Button(deposit_frame, text="Enter", font=("TkMenuFont", 15),
    bg = color, fg = "black", cursor = "hand2", 
    activebackground="#ababab", command=lambda:add_funds.load_funds_frame(root, username, password, users_balance, frame1, frame2, custom_deposit, deposit_frame, counter))
    enter_button.place(x=213, y=470)
    

    #back button
    back_button = tk.Button(deposit_frame, text="Back", font=("TkMenuFont", 14),
    bg = color, fg = "black", cursor = "hand2", 
    activebackground="#ababab", command = lambda:Frames.load_frame2(root, frame1, frame2, username, password, users_balance, counter))
    back_button.place(x=380, y=470)