#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 16:13:25 2024

@author: lamaalabdulwahab
"""

import tkinter as tk

class MyApp:
    def __init__(self, root):
        self.root=root

root = tk.Tk() # Tk() method creates the main root
root.title("My App") # Set title
root.geometry("400x300") # Set size

label = tk.Label(root, text="HELLO!")
label.pack()

entry = tk.Entry(root)
entry.pack()

def on_button_click():
    label.config(text= entry.get() )

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()


root.mainloop() # Launch the window
