import customtkinter
from tkinter import *
from email.message import EmailMessage 
import smtplib
import tkinter as tk
from tkinter import ttk
from random import choice
import datetime
import random
import cv2
from tkinter import messagebox
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

notebook = customtkinter.CTkTabview(app, width=700, height=375)
notebook._segmented_button.configure(font=custom_font)
notebook.add("Homepage")
notebook.add("History")
notebook.add("Send a Message")
notebook.grid(padx=10, pady=10)
notebook._segmented_button.grid(sticky="W")

notebook.set("Homepage")


#History Tab

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

#Send Email Tab

destination = StringVar(notebook.tab("Send a Message"))
subject=StringVar(notebook.tab("Send a Message"))

destination_entry = customtkinter.CTkEntry(notebook.tab("Send a Message"), placeholder_text="Email Address", width=600, height=30, border_width=2, corner_radius=10,textvariable=destination)
destination_entry.place(relx=0.5, rely=0.1, anchor = tk.CENTER)

subject_entry = customtkinter.CTkEntry(notebook.tab("Send a Message"), placeholder_text="Subject", width=600, height=30, border_width=2, corner_radius=10, textvariable=subject)
subject_entry.place(relx=0.5, rely=0.2, anchor = tk.CENTER)

textbox = customtkinter.CTkTextbox(notebook.tab("Send a Message"),width=600, height=200, border_width=2,corner_radius=10)
textbox.place(relx=0.5, rely=0.57, anchor = tk.CENTER)

def send_email():
    receiver = "Auspineda55@gmail.com"
    #Email Structure
    email = EmailMessage()
    email["From"] = receiver
    email["To"] = destination.get()
    email["Subject"] = subject.get()
    email.set_content(str(textbox.get(1.0, 'end')))
    #Send Email
    smtp = smtplib.SMTP_SSL("smtp.gmail.com")
    smtp.login(receiver, "gwmckyegivpmiyyg")
    smtp.sendmail(receiver, destination.get(), email.as_string())
    messagebox.showinfo("Message","Message Sent Successfully ")
    smtp.quit()

send_button = customtkinter.CTkButton(notebook.tab("Send a Message"), text="Send a Message", corner_radius=10,command=send_email)
send_button.place(relx=0.5, rely=0.94, anchor = tk.CENTER)


app.mainloop()