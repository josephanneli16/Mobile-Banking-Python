from database import *
import tkinter as tk
import Frames

"-----------------------------------------------------------"
#Function to take user id and pin input
def take_input(root,username, password, credentials, passwords, frame1, frame2, color):
    username = username.get()
    password = password.get()

    check_credentials(root,username, password, credentials, passwords, frame1, frame2, color)       

"-----------------------------------------------------------"

#checking the input
def check_credentials(root,username, password, credentials, passwords, frame1, frame2, color):
    counter = 0 
    for i in credentials:
        if username == "" and password == "":
            tk.Label(frame1, text = "Empty Username and Password!", bg = color, fg="red", font=("TkMenuFont", 13)).place(x = 128, y = 400)
            break
        if username != credentials[counter] and password != passwords[counter]:
            tk.Label(frame1, text = "Username or Password incorrect!", bg = color, fg="Red", font=("TkMenuFont", 13)).place(x = 128, y = 400)
        if username == credentials[counter] and password == passwords[counter]:
             print("Credentials Verified!")
             Frames.load_frame2(root,frame1, frame2, username, password, balance[counter], counter)

        counter += 1
    
