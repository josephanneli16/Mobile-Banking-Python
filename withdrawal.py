from database import *
import tkinter as tk
from PIL import ImageTk
from tkinter import *
import Frames
import subtract_funds

color = "#ffffff"

def load_withdrawal_frame(root, username, password, balance, frame2, frame1, counter):

    #Withdrawal frame
    withdrawal_frame = tk.Frame(root, width=500, height=600, bg = color)
    withdrawal_frame.grid(row=0, column=0)
    
    Frames.clear_widgets(frame2)
    withdrawal_frame.tkraise()
    withdrawal_frame.pack_propagate(False)

    #bank logo
    logo_img = ImageTk.PhotoImage(file="assets/chase_logo.png")
    logo_widget = tk.Label(withdrawal_frame, image=logo_img, bg = color)
    logo_widget.image = logo_img
    logo_widget.pack()

    #quick withdrawal text
    tk.Label(withdrawal_frame, text = "Quick Withdrawal", bg = color, fg="black", font=("TkMenuFont", 17)).place(x = 160, y = 120)

    #quick Withdrawal button
    ten_button = tk.Button(withdrawal_frame, text=" $ 10 ", font=("TkMenuFont", 17),
    bg = color, fg = "black", cursor = "hand2", 
    activebackground="#ababab", command=lambda:subtract_funds.load_subtract_frame(root, username, password, balance, frame1, frame2, 10, withdrawal_frame, counter))
    ten_button.place(x=160, y=180)

    twenty_button = tk.Button(withdrawal_frame, text=" $ 20 ", font=("TkMenuFont", 17),
    bg = color, fg = "black", cursor = "hand2", 
    activebackground="#ababab", command=lambda:subtract_funds.load_subtract_frame(root, username, password, balance, frame1, frame2, 20, withdrawal_frame, counter))
    twenty_button.place(x=260, y=180)

    fifty_button = tk.Button(withdrawal_frame, text=" $ 50 ", font=("TkMenuFont", 17),
    bg = color, fg = "black", cursor = "hand2", 
    activebackground="#ababab", command=lambda:subtract_funds.load_subtract_frame(root, username, password, balance, frame1, frame2, 50, withdrawal_frame, counter))
    fifty_button.place(x=160, y=230)

    hundred_button = tk.Button(withdrawal_frame, text="$ 100", font=("TkMenuFont", 17),
    bg = color, fg = "black", cursor = "hand2", 
    activebackground="#ababab", command=lambda:subtract_funds.load_subtract_frame(root, username, password, balance, frame1, frame2, 100, withdrawal_frame, counter))
    hundred_button.place(x=260, y=230)

    #Custom Withdrawal text
    tk.Label(withdrawal_frame, text = "Custom Withdrawal", bg = color, fg="black", font=("TkMenuFont", 17)).place(x = 150, y = 350)

    #Custom Withdrawal Entry
    tk.Label(withdrawal_frame, text = "$", bg = color, fg="black", font=("TkMenuFont", 17)).place(x = 105, y = 410)
    custom_withdrawal = tk.Entry(withdrawal_frame, bg = color, fg="black", font=("TkMenuFont", 18))
    custom_withdrawal.place(x = 165, y = 410, width=170, height=35)
    

    #Enter Button
    enter_button = tk.Button(withdrawal_frame, text="Enter", font=("TkMenuFont", 15),
    bg = color, fg = "black", cursor = "hand2", 
    activebackground="#ababab", command=lambda:subtract_funds.load_subtract_frame(root, username, password, balance, frame1, frame2, custom_withdrawal, withdrawal_frame, counter))
    enter_button.place(x=213, y=470)
    

    #back button
    back_button = tk.Button(withdrawal_frame, text="Back", font=("TkMenuFont", 14),
    bg = color, fg = "black", cursor = "hand2", 
    activebackground="#ababab", command = lambda:Frames.load_frame2(root, frame1, frame2, username, password, balance, counter))
    back_button.place(x=380, y=470)