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
import threading  # Import the threading module

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.title("Crack Detection App")
app.geometry("800x600")
app.columnconfigure(0, weight=1)
app.configure(bg="dark")  # Set background color to black

custom_font = customtkinter.CTkFont("Arial", 20, 'bold')

notebook = customtkinter.CTkTabview(app, width=700, height=375)
notebook._segmented_button.configure(font=custom_font)
notebook.add("Detection")
notebook.add("History")
notebook.add("Send a Message")
notebook.grid(padx=10, pady=10)
notebook._segmented_button.grid(sticky="W")

notebook.set("Detection")

# History Tab
my_tree = ttk.Treeview(notebook.tab("History"))
my_tree['columns'] = ("Image","Date and Time","ID","Geo Location")
my_tree.column("#0", width=120, minwidth=25)
my_tree.column("Image", anchor=W, width=120)
my_tree.column("Date and Time", anchor=W, width=120)
my_tree.column("ID", anchor=CENTER, width=80)


my_tree.heading("#0", text="Label", anchor=W)
my_tree.heading("Image", text="Image", anchor=W)
my_tree.heading("Date and Time", text="Date and Time", anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)


e = datetime.datetime.now()
n = random.randint(0,10000)
my_tree.insert(parent='', index='end', iid=0, text=" ", values=("Image"," %s/%s/%s %s:%s:%s" % (e.day, e.month, e.year,e.hour, e.minute, e.second), n))

my_tree.pack(pady=20)

send_button = customtkinter.CTkButton(notebook.tab("History"), text="Submit")
send_button.place(relx=0.5, rely=0.9, anchor = tk.CENTER)

# Send Email Tab
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

# Camera Module
label_camera = Label(notebook.tab("Detection"), bg="gray")  # Set background color of label to gray
label_camera.pack()


# Function to start and stop the camera
def toggle_camera():
    global cap
    global camera_on
    if not hasattr(toggle_camera, 'camera_on'):
        toggle_camera.camera_on = False
    
    if toggle_camera.camera_on:  # If camera is on, turn it off
        stop_camera()
        toggle_camera.camera_on = False
        camera_button.config(text="Start Camera")
    else:  # If camera is off, turn it on
        start_camera_thread()
        toggle_camera.camera_on = True
        camera_button.config(text="Stop Camera")

def start_camera_thread():
    global camera_thread
    camera_thread = threading.Thread(target=start_camera)
    camera_thread.daemon = True  # Set as daemon thread to terminate with the main thread
    camera_thread.start()

def start_camera():
    global cap
    cap = cv2.VideoCapture(0)  # 0 represents the default camera
    if not cap.isOpened():
        messagebox.showerror("Error", "Failed to open camera.")
        return
    else:
        show_frame()

def stop_camera():
    if cap.isOpened():
        cap.release()

def show_frame():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        label_camera.imgtk = imgtk
        label_camera.configure(image=imgtk)
        label_camera.after(10, show_frame)  # Recursive call after 10ms

camera_button = customtkinter.CTkButton(notebook.tab("Detection"), text="Start Camera", corner_radius=10, command=toggle_camera)
camera_button.pack(pady=20)

app.mainloop()
