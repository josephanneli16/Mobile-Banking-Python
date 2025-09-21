import tkinter as tk
from PIL import ImageTk
from tkinter import *
from database import *
from Frames import *

"-----------------------------------------------------------"
color = "#ffffff"


# initiallize app
root = tk.Tk()
root.title("ATM Software")
root.eval("tk::PlaceWindow . center")
frame1 = tk.Frame(root, width=500, height=600, bg = color)
frame2 = tk.Frame(root, width=500, height=600, bg = color)


"-----------------------------------------------------------"

#Create Frame Widget
for frame in (frame1,frame2):
    frame.grid(row=0, column=0)

load_frame1(root, frame1, frame2, balance)

# run app
root.mainloop()