import tkinter as tk
from PIL import ImageTk
from tkinter import *
from database import *
from Frames import *


def update_database(root, frame1, frame2, username, password, users_balance, counter):
    
    balance[counter] = users_balance
    print(balance)
    print(passwords)

    Frames.load_frame1(root, frame1, frame2, users_balance)