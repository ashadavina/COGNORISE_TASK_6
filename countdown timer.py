#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import messagebox
import time

def start_timer():
    try:
        seconds = int(entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number of seconds.")
        return

    while seconds > 0:
        time.sleep(1)
        seconds -= 1

    messagebox.showinfo("Timer", "Time's up!")

root = tk.Tk()
root.title("Countdown Timer")

label = tk.Label(root, text="Enter time (in seconds):")
label.pack()

entry = tk.Entry(root)
entry.pack()

start_button = tk.Button(root, text="Start Timer", command=start_timer)
start_button.pack()

root.mainloop()

