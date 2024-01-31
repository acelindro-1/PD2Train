import customtkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
from random import choice
import datetime
import random
import cv2
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.title("Crack Detection App")
app.geometry("769x399")
app.columnconfigure(0, weight=1)

bg = PhotoImage(file="images/mrt.png")

my_label = Label(app, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

custom_font = customtkinter.CTkFont("Arial", 20, 'bold')

notebook = customtkinter.CTkTabview(app, width=700, height=370)
notebook._segmented_button.configure(font=custom_font)
notebook.add("Homepage")
notebook.add("History")
notebook.add("Send a Message")
notebook.grid(padx=10, pady=10)
notebook._segmented_button.grid(sticky="W")

notebook.set("Homepage")

my_tree = ttk.Treeview(notebook.tab("History"))
my_tree['columns'] = ("Image","Date and Time","ID","Geo Location")
my_tree.column("#0", width=120, minwidth=25)
my_tree.column("Image", anchor=W, width=120)
my_tree.column("Date and Time", anchor=W, width=120)
my_tree.column("ID", anchor=CENTER, width=80)
my_tree.column("Geo Location", anchor=W, width=120)

my_tree.heading("#0", text="Label", anchor=W)
my_tree.heading("Image", text="Image", anchor=W)
my_tree.heading("Date and Time", text="Date and Time", anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Geo Location", text="Geo Location", anchor=W)

e = datetime.datetime.now()
n = random.randint(0,10000)
my_tree.insert(parent='', index='end', iid=0, text=" ", values=("Image"," %s/%s/%s %s:%s:%s" % (e.day, e.month, e.year,e.hour, e.minute, e.second), n))

my_tree.pack(pady=20)

send_button = customtkinter.CTkButton(notebook.tab("History"), text="Submit")
send_button.place(relx=0.5, rely=0.9, anchor = tk.CENTER)

email_add = customtkinter.CTkEntry(notebook.tab("Send a Message"), placeholder_text="Email Address", width=600, height=30, border_width=2,corner_radius=10)
email_add.place(relx=0.5, rely=0.1, anchor = tk.CENTER)

textbox = customtkinter.CTkTextbox(notebook.tab("Send a Message"),width=600, height=200, border_width=2,corner_radius=10)
textbox.place(relx=0.5, rely=0.5, anchor = tk.CENTER)

send_button = customtkinter.CTkButton(notebook.tab("Send a Message"), text="Send a Message")
send_button.place(relx=0.5, rely=0.9, anchor = tk.CENTER)


app.mainloop()