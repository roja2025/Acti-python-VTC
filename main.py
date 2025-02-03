from tkinter import*
from tkinter import Canvas,Tk,Button
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
from datetime import datetime
import os
import json
import threading
import pyaudio
import wave
import webbrowser
import random


root=Tk()
root.title("SignUp Page")
root.iconbitmap("hourglass.ico")


def welcome():

     top1 = Toplevel()
     top1.title("Welcome Page")
     top1.config(bg="pink")



     c2 = Canvas(top1, width=top1.winfo_screenwidth(), height=top1.winfo_screenheight())
     c2.pack(fill="both", expand=True)
     
     img1 = Image.open("wel1.jpg")
     bgphoto1 = ImageTk.PhotoImage(img1.resize((top1.winfo_screenwidth(), top1.winfo_screenheight())))
     

     c2.create_image(0, 0, image=bgphoto1, anchor="nw")
     top1.bgphoto1 = bgphoto1

     c2.create_text(700, 50, text="Virtual Time Capsule", font=("Segoe Script", 30, "bold"), fill="#FFC107",justify=CENTER)
     c2.create_text(220,150,text="Personalized Future Message Box",font=("time new roman",18,"bold"),fill="black")
     t1=""" 
          The Virtual Time Capsule offers a way to capture and preserve moments, memories, and aspirations that will be unlocked in the future. With the Personalized Future Message Box, you can write a message to your future self, reflecting on your current thoughts and dreams, and revisit them at a later date."""
     c2.create_text(720,190,text=t1, width=1300,font=("sans-sarif",12,""),fill="white",justify=LEFT)
     bu1=Button(top1,text="Personalized future message box",command=personal, font=("Times New Roman", 12, "italic", "bold"), bg="#FFC107", fg="black")
     bu1.place(x=150,y=240)

     c2.create_text(145,300,text="Social Time Capsule",font=("time new roman",18,"bold"),fill="black")
     t2=""" 
          The Social Time Capsule allows you to create a shared collection of memories with friends and family, preserving moments together and revisiting them in the future.
     """
     c2.create_text(650,330,text=t2, width=1300,font=("sans-sarif",12,""),fill="white",justify=LEFT)
     bu2=Button(top1,text="Social time capsule",command=social, font=("Times New Roman", 12, "italic", "bold"), bg="#FFC107", fg="black")
     bu2.place(x=150,y=350)

     c2.create_text(180,420,text="Future Generation Capsule",font=("time new roman",18,"bold","italic"),fill="black")
     t3="""
          The Future Generation Capsule gives you the opportunity to leave a legacy for future generations, sharing wisdom, life lessons, and predictions that will be passed down and discovered later."""
     c2.create_text(730,450,text=t3, width=1500,font=("sans-sarif",12,""),fill="white",justify=LEFT)
     bu3=Button(top1,text="Future Generation capsule",command=generation, font=("Times New Roman", 12, "italic", "bold"), bg="#FFC107", fg="black")
     bu3.place(x=150,y=480)

     c2.create_text(210,540,text="Virtual Time Capsule For Events",font=("time new roman",18,"bold"),fill="black")
     t4="""
          For significant life events, The Virtual Time Capsule for Events lets you capture milestones like weddings, birthdays, and anniversaries, creating a digital keepsake of memories to open in the future."""
     c2.create_text(640,570,text=t4, width=1200,font=("sans-sarif",12,""),fill="white",justify=LEFT)
     bu4=Button(top1,text="Capsule for events", font=("Times New Roman", 12, "italic", "bold"), bg="#FFC107", fg="black")
     bu4.place(x=150,y=610)

     c2.create_text(150,670,text="Travel Time Capsule",font=("time new roman",18,"bold"),fill="black")
     t5=""" 
        The Travel Time Capsule lets you save your travel dreams and goals, whether it's a destination or an adventure. You can revisit your travel aspirations and see if you've achieved them when the time comes."""
     c2.create_text(698,698,text=t5, width=1300,font=("sans-sarif",12,""),fill="white",justify=LEFT)
     bu5=Button(top1,text="Capsule for travel",command=travel,font=("Times New Roman", 12, "italic", "bold"),bg="#FFC107", fg="black")
     bu5.place(x=150,y=740)

     top1.mainloop()


img=Image.open("gift1.jpg")
bgphoto=ImageTk.PhotoImage(img.resize((root.winfo_screenwidth(),root.winfo_screenheight())))
bglabel=Label(root,image=bgphoto)
bglabel.place(x=0,y=0,relwidth=1,relheight=1)

# Create canvas
c=Canvas(root,width=5134,height=3355)
c.pack(fill="both",expand=True)
# display image
c.create_image(0,0,image=bgphoto,anchor="nw")
# add text
c.create_text(620,50,text="Virtual Time Capsule",font=("Segoe Script",30,"bold"),fill="white")
c.create_text(600,140,text="SignUp",font=("brush script",20,"bold"),fill="white")
c.create_text(450,200,text="Email",font=("time new roman",18,"bold"),fill="#F2E6D9")
c.place(x=500,y=220)
user_entry=Entry(root,font=("arial",12,"bold"),bg="gray",fg="black")
user_entry.place(x=580,y=189)
c.create_text(474,250,text="Password",font=("time new roman",18,"bold"),fill="#F2E6D9")
p=Entry(root,show="*",font=("arial",12,""),fg="black",bg="gray")
p.place(x=580,y=240)

def signup():
    username=user_entry.get()
    password=p.get()
    if username=='' and password=='':
        messagebox.showerror("Error","Blanks are not allowed")
    elif username=='admin@gmail.com' and password=='123':
        messagebox.showinfo("SignUp","Signup Successfully....")
        welcome()
    else:
        messagebox.showerror("SignUp","Incorrect Email and Password.")
bu=Button(root,text="Signup",bg="#b22222",fg="white",font=("time new roman",10,"italic","bold"),command=signup)
bu.place(x=660,y=300)
c.place(x=0,y=0)

c.create_text(450,400,text="Already have an account?",font=("time new roman",12,"bold"),fill="white")
c.place()
c.create_text(75,555,text="About",font=("time new roman",18,"bold"),fill="white")
t="""
    A virtual time capsule is a digital version of the traditional time capsule, which is a container filled with items meant to be opened at a later date, typically years or decades after being sealed.
    
    A virtual time capsule, instead of physical items, consists of digital content, such as messages, videos, photos, files, and links, that are stored online or in a digital archive.The concept of a virtual time capsule allows people to preserve memories, thoughts, and moments in time for future generations or for themselves to revisit at a specified point in the future. This can be done by using various platforms or websites that offer time capsule services, or by manually storing data in a way that it will remain accessible in the future."""
c.create_text(500,640,text=t, width=950,font=("sans-sarif",12,""),fill="#a9a9a9",justify=LEFT)
c.pack()


def login():
     root.destroy()
     
     top = Tk()
     top.title("Login Page")
     top.config(bg="red")
     top.iconbitmap("hourglass.ico")
    
     
     c1 = Canvas(top, width=top.winfo_screenwidth(), height=top.winfo_screenheight())
     c1.pack(fill="both", expand=True)

    
     img1 = Image.open("gift.jpg")
     bgphoto1 = ImageTk.PhotoImage(img1.resize((top.winfo_screenwidth(), top.winfo_screenheight())))
     c1.create_image(0, 0, image=bgphoto1, anchor="nw")

     user = Entry(top, font=("Arial", 12, "bold"), bg="white", fg="black")
     user.place(x=650, y=189)
     password2= Entry(top, font=("Arial", 12, "bold"), bg="white", fg="black", show="*")
     password2.place(x=650, y=240)

    
     c1.create_text(700, 50, text="Virtual Time Capsule", font=("Segoe Script", 30, "bold"), fill="#ffd700",justify=CENTER)
     c1.create_text(700, 140, text="Login", font=("Brush Script", 20, "bold"), fill="white")
     c1.create_text(570, 200, text="Email", font=("Times New Roman", 18, "bold"), fill="#F2E6D9")
     c1.create_text(570, 250, text="Password",font=("Times New Roman", 18, "bold"), fill="#F2E6D9")

     def login2():
        usernamee=user.get()
        password3=password2.get()
        if usernamee=='' and password3=='':
            messagebox.showerror("Error","Blanks are not allowed")
        elif usernamee=='admin@gmail.com' and password3=='123':
            messagebox.showinfo("Login","Login Successfully....")
            welcome()
        else:
          messagebox.showerror("Login","Incorrect Email and Password")
        
     bu = Button(top, text="Login", font=("Times New Roman", 10, "italic", "bold"), bg="#8b0000", fg="white",command=login2)
     bu.place(x=720, y=300)
     top.mainloop()

buu=Button(text="Login",font=("time new roman",10,"italic","bold"),bg="#8b0000",fg="white",command=login)
buu.place(x=590,y=387)


def personal():
    top2 = Toplevel()
    top2.title("Personalized Future Message Box")
    top2.config(bg="pink")
    top2.iconbitmap("hourglass.ico")
    c3 = Canvas(top2, width=top2.winfo_screenwidth(), height=top2.winfo_screenheight())
    c3.pack(fill="both", expand=True)
    img1 = Image.open("personall.jpg")
    bgphoto1 = ImageTk.PhotoImage(img1.resize((top2.winfo_screenwidth(), top2.winfo_screenheight())))
    c3.create_image(0, 0, image=bgphoto1, anchor="nw")
    c3.create_text(650, 20, text="Virtual Time Capsule", font=("Segoe Script", 20, "bold"), fill="#FFC107", justify=CENTER)
    c3.create_text(645, 50, text="Personalized Future Message Box", width=1300, font=("sans-serif", 12, "bold"), fill="black", justify=CENTER)
    c3.create_text(650, 20, text="Virtual Time Capsule", font=("Segoe Script", 20, "bold"), fill="#FFC107", justify=CENTER)
    c3.create_text(645, 50, text="Personalized Future Message Box", width=1300, font=("sans-serif", 12, "bold"), fill="black", justify=CENTER)
    t11 = """ Send a Message to Your Future Self :
    Ever wondered what your future self would think of your present? With the Personalized Future Message Box, you can write a message to yourself, save it, and set a date in the future to read it. This is your space to store thoughts, hopes, dreams, or even predictions for the future."""
    c3.create_text(710, 110, text=t11, width=1400, font=("Times New Roman", 15), fill="black", justify=LEFT)
   
# Function to show the message and image
    def show_message(name, message, image_path,future_time_str):
        top = Toplevel(top2)
        top.title("Your Future Message")
        top.iconbitmap("hourglass.ico")

        # Display Image
        try:
            image = Image.open(image_path)
            image = image.resize((300, 300))  # Resize image to fit in the window
            img = ImageTk.PhotoImage(image)
            img_label = Label(top, image=img)
            img_label.image = img  # Keep reference to the image
            img_label.pack()
        except:
            messagebox.showerror("Image Error", "Unable to load image.")

        # Display message
        message_label = Label(top, text=f"Hello, {name}!\nYour message is:\n{message} \n Date & Time :\n {future_time_str}", font=("Helvetica", 12))
        message_label.pack(pady=20)
        close_button = Button(top, text="Close", command=top.destroy)
        close_button.place(x=50,y=550)
 

    # Function to set the timer for the future message
    def set_timer():
        try:
            future_time_str = f"{date_entry.get()} {time_entry.get()}"
            future_time = datetime.datetime.strptime(future_time_str, "%Y-%m-%d %H:%M")
            current_time =datetime.datetime.now()
            
            delay_seconds = (future_time - current_time).total_seconds()
            if future_time >=current_time:
                   data = {
                    "name": name_entry.get(),
                    "message": message_entry.get("1.0", "end-1c"),
                    "image_path": image_path,
                    "future_time": future_time_str
                    }

                   file_path = "personal_message.json"
                   with open(file_path, "w") as file:
                    json.dump(data, file)

                 # Set the timer to show the message at the specified future time
                    timer = threading.Timer(delay_seconds, open_message)
                    timer.start()

                    # Feedback to user
                    messagebox.showinfo("Timer Set", f"Your message will appear on {future_time_str}.")
            else:
               messagebox.showerror("Invalid Time", "Please choose a future time.")
                
        except ValueError:
            messagebox.showerror("Invalid Date and Time Format", "Please use the correct format (YYYY-MM-DD HH:MM).")
            return
    # Function to open the message at the specified time
    def open_message():
        try:
            # Read data from the file
            file_path = "personal_message.json"
            if os.path.exists(file_path):
                with open(file_path, "r") as file:
                    data = json.load(file)
                
                # Show the message
                show_message(data["name"], data["message"], data["image_path"],data["future_time"])
                
            else:
                messagebox.showerror("File Error", "Message file not found.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        

    # Function to select an image file
    def select_image():
        global image_path
        image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])
        if image_path:
                image_path = image_path
                # Display the image in the GUI
                img = Image.open(image_path)
                img.thumbnail((100, 100))  # Resize the image for display
                img_display = ImageTk.PhotoImage(img)

                image_label.config(image=img_display)
                image_label.image = img_display

            

    # Creating the main window
    c3.create_text(500, 220, text="Enter Your Name:", font=("Helvetica", 12, "bold"), fill="black")
    name_entry = Entry(top2, font=("Helvetica", 8,""))
    name_entry.place(x=620, y=210)

    c3.create_text(510,270, text="Enter Your Message:", font=("Helvetica", 12, "bold"))
    message_entry = Text(top2, height=3, width=50, font=("Helvetica", 10))
    message_entry.place(x=620, y=260)

    c3.create_text(520, 350, text="Set Date (YYYY-MM-DD):", font=("Helvetica", 12, "bold"))
    date_entry = Entry(top2, font=("Helvetica", 10))
    date_entry.place(x=620, y=340)

    c3.create_text(500, 400, text="Set Time (HH:MM):", font=("Helvetica", 12, "bold"))
    time_entry = Entry(top2, font=("Helvetica", 10))
    time_entry.place(x=620, y=395)

    c3.create_text(510, 448, text="Choose File to Store:", font=("Helvetica", 12, "bold"), fill="black")
    upload_button = Button(top2, text="Upload Image", command=select_image, font=("Helvetica",8,""))
    upload_button.place(x=620, y=448)

    image_label = Label(top2, text="No image selected", font=("Helvetica", 8, ""))
    image_label.place(x=800,y=420)
    
    # Buttons to save or open the capsule
    save_button = Button(top2, text="Save Time Capsule", command=set_timer, font=("Helvetica", 8, "bold", "italic"))
    save_button.place(x=620, y=530)

    open_button = Button(top2, text="Set&Preview Capsule", command=open_message, font=("Helvetica", 8, "bold", "italic"))
    open_button.place(x=780, y=530)
    
    top2.mainloop()
   



def social():


    # Function to save the message and image
    messages_data = []

    # Folder to store uploaded images
    image_folder = "images"
    os.makedirs(image_folder, exist_ok=True)

    # Function to save the message and image
    def save_message():
        message = message_text.get("1.0", "end-1c")
        date_str = date_entry.get()
        time_str = time_entry.get()
        recipient = recipient_entry.get()

        # Combine the date and time into a single datetime string
        try:
            full_datetime_str = f"{date_str} {time_str}"
            unlock_datetime =datetime.datetime.strptime(full_datetime_str, '%Y-%m-%d %H:%M')
            current_time =datetime.datetime.now()
            delay_seconds = (unlock_datetime- current_time).total_seconds()
            # if future_time >=current_time:
            if unlock_datetime >= current_time:
                messagebox.showinfo("Info", "The date and time save successfully.....!")
                return
            else:
                 messagebox.showerror("Alert", "The date and time must be in the future!")
                 return
        except ValueError:
            messagebox.showerror("Invalid Date and Time Format", "Please use the correct format (YYYY-MM-DD HH:MM).")
        

        # Prepare message dictionary to store the message data
        new_message = {
            "message": message,
            "datetime": unlock_datetime.strftime('%Y-%m-%d %H:%M'),  # Store full datetime
            "image_path": image_path if image_path else None,  # Store image path if any
            "recipient": recipient  # Store recipient
        }

        # Add the new message to the in-memory list
        messages_data.append(new_message)
        
        # Save image to folder if exists
        if image_path:
            img_name = os.path.basename(image_path)
            img_dest_path = os.path.join(image_folder, img_name)
            img = Image.open(image_path)
            img.save(img_dest_path)

        messagebox.showinfo("Message Saved", "Your message and image have been saved successfully!")

    # Function to open the capsule (retrieve messages)
    def retrieve_message():
        current_datetime =datetime.datetime.now()
        unlocked_messages = []

        # Iterate through stored messages and unlock those whose time has come
        for msg in messages_data:
            stored_datetime = datetime.datetime.strptime(msg['datetime'], '%Y-%m-%d %H:%M')

            # If the stored datetime is today and the current time is equal to or later than the stored time
            if stored_datetime.date() == current_datetime.date():
                if stored_datetime <= current_datetime:
                    unlocked_messages.append(msg)
            # If the stored datetime is in the future
            elif stored_datetime > current_datetime:
                unlocked_messages.append(msg)

        if unlocked_messages:
            open_message_window(unlocked_messages)
        else:
            messagebox.showinfo("No Messages", "No messages are unlocked for now.")

    # Function to open a window to display unlocked messages
    def open_message_window(unlocked_messages):
        top = Toplevel(root)
        top.title("Opened Capsule")
        top.geometry("500x500")
        top.iconbitmap("hourglass.ico")

        # Create a Scrollable Frame
        canvas = Canvas(top)
        scrollbar = Scrollbar(top, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas)
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Display each message in the unlocked list
        for msg in unlocked_messages:
            msg_label = Label(scrollable_frame, text=f"Message to {msg['recipient']}:\n{msg['message']}\nDate and Time: {msg['datetime']}")
            msg_label.pack(pady=10, anchor="w")

            if msg['image_path']:
                img_path = os.path.join(image_folder, os.path.basename(msg['image_path']))
                try:
                    img = Image.open(img_path)
                    img.thumbnail((150, 150))
                    img_display = ImageTk.PhotoImage(img)
                    img_label = Label(scrollable_frame, image=img_display)
                    img_label.image = img_display  # Keep a reference to avoid garbage collection
                    img_label.pack(pady=10)
                except Exception as e:
                    print(f"Error loading image: {e}")

        close_button = Button(top, text="Close", command=top.destroy)
        close_button.pack(pady=10)


        def share_capsule():
            t = Toplevel()
            t.title("Share Capsule Contents")
            t.iconbitmap("hourglass.ico")
            c61= Canvas(t, width=t.winfo_screenwidth(), height=t.winfo_screenheight())
            c61.pack(fill="both", expand=True)
            c61.create_text(750, 70, text=" Share Virtual Time Capsule ",font=("sans-serif", 15, "bold"))

            def email():
                share_url=f"https://mail.google.com"
                webbrowser.open(share_url)
            c61.create_text(690, 140, text="Share wih Gmail", font=("Times New Roman", 13)) 
            Button(t,text="Gmail",command=email,font=("Times New Roman",8,"")).place(x=800,y=130)

            def insta():
                insta_url=f"https://www.instagram.com" 
                webbrowser.open(insta_url)
            c61.create_text(700, 210, text="Share wih Instagram", font=("Times New Roman", 13))
            Button(t,text="Instagram",command=insta,font=("Times New Roman",8,"")).place(x=800,y=200)

            def face():
                face_url=f" https://www.facebook.com"
                webbrowser.open(face_url)
            c61.create_text(700, 280, text="Share wih FaceBook", font=("Times New Roman", 13)) 
            Button(t,text="Facebook",command=face,font=("Times New Roman",8,"")).place(x=800,y=270)

            def twi():
                twitter_url=f"https://twitter.com"
        
                webbrowser.open(twitter_url)
            c61.create_text(690, 350, text="Share wih Twitter",font=("Times New Roman", 13)) 
            Button(t,text="Twitter",command=twi,font=("Times New Roman",8,"")).place(x=800,y=340)
            
            def whats():
                whatsapp_url=f"https://web.whatsapp.com/"
                webbrowser.open(whatsapp_url)
            c61.create_text(700, 420, text="Share wih WhatsApp",font=("Times New Roman", 13)) 
            Button(t,text="Whatsapp",command=whats,font=("Times New Roman",8,"")).place(x=800,y=410)

        share= Button(top, text="share", command=share_capsule)
        share.pack(pady=10,padx=25)

    # Function to upload an image
    def upload_image():
        global image_path
        file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            image_path = file_path
            # Display the image in the GUI
            img = Image.open(image_path)
            img.thumbnail((100, 100))  # Resize the image for display
            img_display = ImageTk.PhotoImage(img)

            image_label.config(image=img_display)
            image_label.image = img_display  # Keep a reference to avoid garbage collection
    



    top3 = Toplevel()
    top3.title("Social Time Capsule")
    top3.config(bg="Lavender")
    top3.iconbitmap("hourglass.ico")

    c4 = Canvas(top3, width=top3.winfo_screenwidth(), height=top3.winfo_screenheight())
    c4.pack(fill="both", expand=True)
    img1 = Image.open("social.jpg")
    bgphoto1 = ImageTk.PhotoImage(img1.resize((top3.winfo_screenwidth(), top3.winfo_screenheight())))
    c4.create_image(0, 0, image=bgphoto1, anchor="nw")

    c4.create_text(650, 20, text="Virtual Time Capsule", font=("Segoe Script", 20, "bold"), fill="#FFC107", justify=CENTER)
    c4.create_text(645, 50, text="Social Time Capsule", width=1300, font=("sans-serif", 17, "bold"), fill="black", justify=CENTER)
    t21 = """"Create a Shared Memory for the Future"
    Life is more meaningful when shared with others, and so is a Social Time Capsule. Gather your friends, family, or community and collaborate to create a time capsule that will live on for years. Together, you’ll create a digital archive of memories, thoughts, and reflections that will be unlocked in the future."""
    c4.create_text(710, 120, text=t21, width=1400, font=("Times New Roman", 15), fill="black", justify=LEFT) 
           
   
   

    # Create and place widgets (labels, buttons, text area, etc.)
    c4.create_text(400, 210, text="Write your message :" ,font=("time new roman", 13, "bold"), fill="white")
    message_text = Text(top3, height=3, width=40)
    message_text.place(x=600,y=200)

    c4.create_text(430, 280, text="Enter the date (YYYY-MM-DD):", font=("time new roman", 13, "bold"),fill="white")
    date_entry = Entry(top3, width=20)
    date_entry.place(x=600,y=270)
    
    c4.create_text(405, 340, text="Enter the time (HH:MM):", font=("time new roman", 13, "bold"), fill="white")
    time_entry = Entry(top3)
    time_entry.place(x=600,y=330)

    c4.create_text(400, 400, text="Enter recipient's name:", font=("time new roman", 13, "bold"), fill="white")
    recipient_entry = Entry(top3)
    recipient_entry.place(x=600,y=390)

    upload_button = Button(top3, text="Upload Image", command=upload_image)
    upload_button.place(x=600,y=485)

    image_label = Label(top3)
    image_label.place(x=400,y=450)

    save_button = Button(top3, text="Save Message", command=save_message)
    save_button.place(x=600,y=560)

    retrieve_button = Button(top3, text="Retrieve Unlocked Messages", command=retrieve_message)
    retrieve_button.place(x=700,y=560)

    # retrieve_button = Button(top3, text="Share", command=share_capsule)
    # retrieve_button.place(x=900,y=560)

    top3.mainloop()



global generation
def generation():
    top4 = Toplevel()
    top4.title("Future Generation Capsule")
    top4.config(bg="Lavender")
    top4.iconbitmap("hourglass.ico")
    
    img1 = Image.open("future2.jpg")
    bgphoto1 = ImageTk.PhotoImage(img1.resize((top4.winfo_screenwidth(), top4.winfo_screenheight())))
    
    c5 = Canvas(top4, width=top4.winfo_screenwidth(), height=top4.winfo_screenheight())
    c5.pack(fill="both", expand=True)
    c5.create_image(0, 0, image=bgphoto1, anchor="nw")

    c5.create_text(650, 20, text="Virtual Time Capsule", font=("Segoe Script", 20, "bold"), fill="#FFC107", justify=CENTER)
    c5.create_text(645, 70, text="Future Generation Capsule", width=1300, font=("sans-serif", 15, "bold"), fill="white", justify=CENTER)
    
    t31 = """Leave a Legacy for Future Generations...
    Future Generation Capsule with these elements, you give future generations a treasure trove of wisdom, personal history, and insights that will connect them to your time, your legacy, and the journey that has led them to where they are. This is not just a collection of memories, but a way to influence the future, inspire others, and preserve your legacy for years to come.\tYour write topics in like Personal Messages and Life Lessons,Future Predictions, Cultural and Technological Context,etc..."""
    c5.create_text(710, 150, text=t31, width=1400, font=("Times New Roman", 15), fill="white", justify=LEFT) 

    capsule_contents = ""
    capsule_files = []
    capsule_date_time = ""

    def create_capsule():
        global capsule_contents, capsule_files, capsule_date_time
        
        # Get the name, message, date, time, and files
        name = entry_name.get().strip()
        recivername = reciver_name.get().strip()
        message = entry_message.get("1.0", END).strip()
        date = entry_date.get().strip()
        time = entry_time.get().strip()

        # Validate input
        if not name or not message:
            messagebox.showwarning("Input Error", "Please provide both your name and a message for the future.")
            return

        if not date or not time:
            messagebox.showwarning("Date/Time Error", "Please provide both a date and a time.")
            return

        # Combine date and time and convert to datetime object
        try:
            future_date_time = datetime.datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
        except ValueError:
            messagebox.showwarning("Invalid Date/Time", "Please enter a valid date and time in the format YYYY-MM-DD HH:MM.")
            return

        # Validate if the future date/time is really in the future
        current_time = datetime.datetime.now()
        if future_date_time <= current_time:
            messagebox.showwarning("Future Date/Time Error", "The date and time must be in the future.")
            return

        # Collect selected items
        selected_items = []
        if var_advice.get():
            selected_items.append("Advice")
        if var_photos.get():
            selected_items.append("Photos/Videos")
        if var_technology.get():
            selected_items.append("Newspaper/Media")
        if var_artifacts.get():
            selected_items.append("Artifacts")

        # Store the capsule contents
        capsule_contents = f"Future Generation Capsule\n\nName: {name}\nReceiver Name: {recivername}\nMessage: {message}\n"
        capsule_contents += f"Future Date: {date} Time: {time}\n"
        capsule_contents += "Items to include:\n"
        if selected_items:
            capsule_contents += "\n".join(selected_items)
        else:
            capsule_contents += "No items selected."

        capsule_date_time = future_date_time  # Store the future date/time as a datetime object

        # Show uploaded files
        capsule_files = selected_files

        # Show the capsule content in a new Toplevel window
        show_capsule_window(capsule_contents, capsule_files, capsule_date_time)

    def open_capsule():
        global capsule_contents, capsule_files, capsule_date_time
        
        # Check if the capsule can be opened
        if not capsule_contents:
            messagebox.showwarning("No Capsule", "No capsule has been created yet.")
            return
        
        current_time = datetime.datetime.now()
        
        # If the current time is less than the set future date/time, show a warning
        if current_time <= capsule_date_time:
            messagebox.showwarning("Too Early", f"The capsule can only be opened after the specified future time: {capsule_date_time.strftime('%Y-%m-%d %H:%M')}.")
            return
        
        # Show the capsule content in a new Toplevel window
        show_capsule_window(capsule_contents, capsule_files, capsule_date_time)

    def upload_files():
        # Allow user to upload files (photos/videos)
        files = filedialog.askopenfilenames(title="Select photos/videos", filetypes=[("All Files", "*.*")])
        selected_files.extend(files)
        
        # Update the label with the file path(s)
        file_paths = '\n'.join(files)
        label_file_path.config(text=file_paths)
        
        # Show image or video preview
        show_file_preview(files)
        
        messagebox.showinfo("Info","Files uploaded successfully")

    def set_current_datetime():
        # Set the current date and time in the input fields
        now = datetime.datetime.now()
        entry_date.delete(0, END)
        entry_date.insert(0, now.strftime("%Y-%m-%d"))
        entry_time.delete(0, END)
        entry_time.insert(0, now.strftime("%H:%M"))
        messagebox.showinfo("Info","Set Time and Date")

    def show_capsule_window(capsule_contents, capsule_files, capsule_date_time):
        # Create a Toplevel window to display the capsule content
        capsule_window = Toplevel(top4)
        capsule_window.title("Capsule Contents")
        capsule_window .iconbitmap("hourglass.ico")

        # Show capsule text content
        label_capsule = Label(capsule_window, text=capsule_contents, justify=LEFT, anchor="w", width=50, height=10)
        label_capsule.place(x=20, y=20)

        # Display the future date and time
        label_datetime = Label(capsule_window, text=f"Date and Time Set for: {capsule_date_time.strftime('%Y-%m-%d %H:%M')}", anchor="w", width=50)
        label_datetime.place(x=20, y=180)

        # Display uploaded files (photos/videos)
        if capsule_files:
            label_files = Label(capsule_window, text="Uploaded Photos/Videos:", anchor="w", width=50)
            label_files.place(x=20, y=220)
            global file, idx
            for idx, file in enumerate(capsule_files):
                file_name = file.split('/')[-1]  # Get file name from path
                label_file_name = Label(capsule_window, text=file_name, anchor="w", width=50)
                label_file_name.place(x=20, y=250 + (idx * 30))
                
                # Display images (if any)
                if file.lower().endswith(('png', 'jpg', 'jpeg', 'gif')):
                    try:
                        img = Image.open(file)
                        img.thumbnail((100, 100))  # Resize image
                        img_tk = ImageTk.PhotoImage(img)
                        
                        label_img = Label(capsule_window, image=img_tk)
                        label_img.image = img_tk  # Keep a reference
                        label_img.place(x=20, y=300 + (idx * 120))
                    except Exception as e:
                        print(f"Error loading image {file}: {e}")
                
                # Display videos (if any, just filenames in this case)
                elif file.lower().endswith(('mp4', 'avi', 'mov', 'mkv')):
                    label_video_name = Label(capsule_window, text=f"Video: {file_name}", anchor="w", width=50)
                    label_video_name.place(x=20, y=300 + (idx * 120))
                    # Here, you'd implement video playing functionality using external libraries if desired

        else:
            label_no_files = Label(capsule_window, text="No photos/videos uploaded.", anchor="w", width=50)
            label_no_files.place(x=20, y=250)

        # Close button for  Toplevel window
        button_close = Button(capsule_window, text="Close", command=capsule_window.destroy)
        button_close.place(x=20, y=550)
        def share_capsule():
            t = Toplevel()
            t.title("Share Capsule Contents")
            t.geometry("900x900")
            t.iconbitmap("hourglass.ico")
            c61= Canvas(t, width=t.winfo_screenwidth(), height=t.winfo_screenheight())
            c61.pack(fill="both", expand=True)
            c61.create_text(750, 70, text=" Share Virtual Time Capsule ",font=("sans-serif", 15, "bold"))

            def email():
                share_url=f"https://mail.google.com"
                webbrowser.open(share_url)
            c61.create_text(690, 140, text="Share wih Gmail", font=("Times New Roman", 13)) 
            Button(t,text="Gmail",command=email,font=("Times New Roman",8,"")).place(x=800,y=130)

            def insta():
                insta_url=f"https://www.instagram.com" 
                webbrowser.open(insta_url)
            c61.create_text(700, 210, text="Share wih Instagram", font=("Times New Roman", 13))
            Button(t,text="Instagram",command=insta,font=("Times New Roman",8,"")).place(x=800,y=200)

            def face():
                face_url=f" https://www.facebook.com"
                webbrowser.open(face_url)
            c61.create_text(700, 280, text="Share wih FaceBook", font=("Times New Roman", 13)) 
            Button(t,text="Facebook",command=face,font=("Times New Roman",8,"")).place(x=800,y=270)

            def twi():
                twitter_url=f"https://twitter.com"
        
                webbrowser.open(twitter_url)
            c61.create_text(690, 350, text="Share wih Twitter",font=("Times New Roman", 13)) 
            Button(t,text="Twitter",command=twi,font=("Times New Roman",8,"")).place(x=800,y=340)
            
            def whats():
                whatsapp_url=f"https://web.whatsapp.com/"
                webbrowser.open(whatsapp_url)
            c61.create_text(700, 420, text="Share wih WhatsApp",font=("Times New Roman", 13)) 
            Button(t,text="Whatsapp",command=whats,font=("Times New Roman",8,"")).place(x=800,y=410)
        share = Button(capsule_window, text="Share", command=share_capsule)
        share.place(x=100, y=550)


    def show_file_preview(files):
        # Show preview of the first image/video in the list
        for file in files:
            file_name = os.path.basename(file)
            file_extension = file_name.split('.')[-1].lower()

            # Clear previous previews
            for widget in frame_preview.winfo_children():
                widget.destroy()

            if file_extension in ['png', 'jpg', 'jpeg', 'gif']:
                # Image file preview
                try:
                    img = Image.open(file)
                    img.thumbnail((100, 100))  # Resize the image
                    img_tk = ImageTk.PhotoImage(img)
                    label_img_preview = Label(frame_preview, image=img_tk)
                    label_img_preview.image = img_tk  # Keep a reference to avoid garbage collection
                    label_img_preview.pack(padx=1, pady=1)
                except Exception as e:
                    messagebox.showwarning("Error", f"Error loading image: {e}")
            elif file_extension in ['mp4', 'avi', 'mov', 'mkv']:
                # Video file preview (only show the filename for now)
                label_video_preview = Label(frame_preview, text=f"Video: {file_name}", font=("Arial", 12))
                label_video_preview.pack()


    # Initialize selected files list
    selected_files = []

    c5.create_text(200, 250, text="Enter your Name :", font=("Times New Roman", 15,"bold"), fill="white") 
    entry_name = Entry(top4, width=40)
    entry_name.place(x=300, y=240)
    
    c5.create_text(700, 250, text="Enter Receiver Name :", font=("Times New Roman", 15,"bold"), fill="white")    
    reciver_name = Entry(top4, width=50)
    reciver_name.place(x=800, y=240)

    c5.create_text(210, 300, text="Write a message for\nfuture generations:", font=("Times New Roman", 15,"bold"), fill="white") 
    entry_message = Text(top4, width=50, height=5, bg="light gray")
    entry_message.place(x=300, y=280)

    c5.create_text(180, 390, text="Select future\ndate and time:", font=("Times New Roman", 15,"bold"), fill="white")
    entry_date = Entry(top4, width=20)
    entry_date.place(x=320, y=390)

    entry_time = Entry(top4, width=20)
    entry_time.place(x=450, y=390)

    # Button to set current date and time
    set_current_btn = Button(top4, text="Set Date/Time", command=set_current_datetime, font=("Times New Roman", 8,""))
    set_current_btn.place(x=600, y=390)

    # Section for Image/Video Upload
    upload_button = Button(top4, text="Upload Photos/Videos", command=upload_files, font=("Times New Roman", 8,""))
    upload_button.place(x=450, y=450)

    # Label to show file path
    label_file_path = Label(top4, text="", font=("Times New Roman", 10), fg="gray")
    label_file_path.place(x=600, y=450)

    # Frame to display image/video preview
    frame_preview = Frame(top4)
    frame_preview.place(x=890, y=400)

    # Section for selecting items to include in the capsule
    c5.create_text(215, 500, text="Select items to\ninclude in the capsule:", font=("Times New Roman", 15,"bold"), fill="white")
    
    var_technology = BooleanVar()
    check_technology = Checkbutton(top4, text="Technology Item (e.g., gadgets, devices)", variable=var_technology)
    check_technology.place(x=320, y=500)
    
    
    var_photos = BooleanVar()
    check_photos = Checkbutton(top4, text="Photos/Videos", variable=var_photos)
    check_photos.place(x=590, y=500)

    var_advice = BooleanVar()
    check_newspaper = Checkbutton(top4, text="Advice", variable=var_advice)
    check_newspaper.place(x=720, y=500)

    var_artifacts = BooleanVar()
    check_artifacts = Checkbutton(top4, text="Artifacts (e.g., books, toys)", variable=var_artifacts)
    check_artifacts.place(x=820, y=500)

    # Button to create the capsule
    button_create = Button(top4, text="Set&Preview Capsule", command=create_capsule,bg="navy",fg="white",font=("Times New Roman", 10,"bold"))
    button_create.place(x=500, y=600)

    # Button to open the capsule
    button_open = Button(top4, text="Open Capsule", command=open_capsule,bg="navy",fg="white",font=("Times New Roman", 10,"bold"))
    button_open.place(x=650, y=600)
    top4.mainloop()
generation()



def event():
    top5 = Toplevel()
    top5.title("Event Capsule")
    top5.config(bg="Lavender")
    top5.iconbitmap("hourglass.ico")
    
    img1 = Image.open("event.jpeg")
    bgphoto1 = ImageTk.PhotoImage(img1.resize((top5.winfo_screenwidth(), top5.winfo_screenheight())))

    c6 = Canvas(top5, width=top5.winfo_screenwidth(), height=top5.winfo_screenheight())
    c6.pack(fill="both", expand=True)
    c6.create_image(0, 0, image=bgphoto1, anchor="nw")

    c6.create_text(650, 20, text="Virtual Time Capsule", font=("Segoe Script", 20, "bold"), fill="#FFC107", justify=CENTER)
    c6.create_text(645, 90, text="Virtual Time Capsule For Events", width=1300, font=("sans-serif", 15, "bold"), fill="white", justify=CENTER)
    
    t31 = """Celebrate Life's Milestones with a Time Capsule
    Major milestones in life deserve to be remembered in a special way. With the Virtual Time Capsule for Events, you can capture the emotions and celebrations of any special event—whether it's a wedding, anniversary, or birthday and preserve them for a future date."""
    c6.create_text(710, 170, text=t31, width=1400, font=("Times New Roman", 15), fill="white", justify=LEFT) 

    # Variables for storing event details
    event_name = StringVar()
    event_date = StringVar()
    messages = []
    images = []
    audio_files = []
    video_files = []
    capsule_open_date = None

    # Function to add a message
    def add_message(message_entry):
        message = message_entry.get("1.0", "end-1c")  # Get the entire content of the Text widget
        if message.strip():  # Check if the message is not empty after stripping whitespaces
            messages.append(message)
            # message_entry.delete("1.0", "end")  # Clear the entry after adding the message
            messagebox.showinfo("Message Added", "Your message has been added!")
        else:
            messagebox.showwarning("Empty Message", "Please enter a message before adding.")

    # Function to add voice message
    def record_voice_message():
        try:
            chunk = 1024  # Record in chunks of 1024 samples
            sample_format = pyaudio.paInt16  # 16 bits per sample
            channels = 1  # Mono recording
            rate = 44100  # Record at 44.1kHz
            frames_per_buffer = chunk

            p = pyaudio.PyAudio()
            print("Recording...")

            stream = p.open(format=sample_format,
                            channels=channels,
                            rate=rate,
                            input=True,
                            frames_per_buffer=frames_per_buffer)

            frames = []

            for i in range(0, int(rate / chunk * 10)):  # Record for 10 seconds
                data = stream.read(chunk)
                frames.append(data)

            stream.stop_stream()
            stream.close()
            p.terminate()

            file_path = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("WAV Files", "*.wav")])
            if file_path:
                with wave.open(file_path, 'wb') as wf:
                    wf.setnchannels(channels)
                    wf.setsampwidth(p.get_sample_size(sample_format))
                    wf.setframerate(rate)
                    wf.writeframes(b''.join(frames))
                audio_files.append(file_path)
                messagebox.showinfo("Voice Message", "Your voice message has been saved!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while recording: {e}")

    # Function to upload image
    def upload_image():
        file_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            images.append(file_path)
            image = Image.open(file_path)
            image = image.resize((50, 50))  # Resize image to fit UI
            photo = ImageTk.PhotoImage(image)
            image_label.config(image=photo)
            image_label.image = photo  # Keep a reference to the image object
            messagebox.showinfo("Image Uploaded", "Your image has been added to the time capsule!")

    # Function to upload video
    def upload_video():
        file_path = filedialog.askopenfilename(title="Select a Video", filetypes=[("Video Files", "*.mp4;*.avi;*.mov")])
        if file_path:
            video_files.append(file_path)
            messagebox.showinfo("Video Uploaded", "Your video has been added to the time capsule!")

    # Function to start the time capsule opening party
    def start_capsule_party():
        messagebox.showinfo("Time Capsule Opening Party", "Your time capsule party has started! Join via your preferred video call platform.")
        meeting_link = f"https://zoom.us/j/{random.randint(1000000000, 9999999999)}"
        webbrowser.open(meeting_link)

    # Function to save the capsule
    def save_capsule():
        global capsule_open_date
        try:
            event_name_str = event_name.get()
            event_date_str = event_date.get()

            if not event_name_str or not event_date_str:
                raise ValueError("Event name and date cannot be empty!")

            # Parse the event date string into a datetime object
            capsule_open_date = datetime.strptime(event_date_str, "%Y-%m-%d %H:%M")

            # Ensure the capsule opening date is in the future
            if capsule_open_date <= datetime.now():
                messagebox.showerror("Error", "The opening date must be in the future!")
                return

            # Create a capsule details dictionary
            capsule_data = {
                "event_name": event_name_str,
                "event_date": capsule_open_date.strftime("%Y-%m-%d %H:%M"),
                "messages": messages,
                "images": images,
                "audio_files": audio_files,
                "video_files": video_files
            }

            # Save the capsule (for demo, we simply print the details, but you can write it to a file)
            print(f"Capsule saved! It will open on {capsule_open_date}")
            print(capsule_data)

            messagebox.showinfo("Capsule Saved", f"Your time capsule has been saved! It will open on {capsule_open_date.strftime('%Y-%m-%d %H:%M')}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving: {e}")

    # Function to force open the capsule (for "Must Open" button)
    def must_open_capsule():
        global capsule_open_date
        if capsule_open_date is None:
            messagebox.showerror("Error", "No capsule date has been set!")
            return

        # Check if the current time is equal to or after the capsule opening date
        if datetime.now() >= capsule_open_date:
            show_capsule_contents()  # Show the capsule contents
        else:
            # Inform the user they need to wait until the specified time
            messagebox.showinfo("Wait for Opening", f"The capsule will open on {capsule_open_date.strftime('%Y-%m-%d %H:%M')}. Please wait until that time.")
            
    def show_capsule_contents():
        # Create a new Toplevel window to display the capsule contents
        top = Toplevel()
        top.title("Capsule Contents")
        top.geometry("500x600")
        top.iconbitmap("hourglass.ico")

        # Event name and date
        event_name_str = event_name.get()
        contents = f"Event: {event_name_str}\n"
        contents += f"Event Date: {capsule_open_date.strftime('%Y-%m-%d %H:%M')}\n\n"

        # Messages
        contents += "\nMessages:\n"
        contents += "\n".join(messages) + "\n"

        # Create a Text widget to display contents
        text = Text(top, wrap="word", width=60, height=10)
        text.insert(END, contents)
        text.config(state=DISABLED)  # Make it read-only
        text.place(x=10, y=10)

        # Display images if any
        if images:
            img_label = Label(top, text="Images:").place(x=10, y=200)
            y_offset = 230
            for img_path in images:
                image = Image.open(img_path)
                image = image.resize((100, 100))  # Resize images to fit
                photo = ImageTk.PhotoImage(image)
                img_label = Label(top, image=photo)
                img_label.image = photo  # Keep reference to avoid garbage collection
                img_label.place(x=10, y=y_offset)
                y_offset += 110

        # Display audio files if any
        if audio_files:
            audio_label = Label(top, text="Audio Files:").place(x=10, y=y_offset)
            y_offset += 30
            for audio_file in audio_files:
                audio_label = Label(top, text=audio_file).place(x=10, y=y_offset)
                y_offset += 30

        # Display video files if any
        if video_files:
            video_label = Label(top, text="Video Files:").place(x=10, y=y_offset)
            y_offset += 30
            for video_file in video_files:
                video_label = Label(top, text=video_file).place(x=10, y=y_offset)
                y_offset += 30
        button_close = Button(top, text="Close", command=top.destroy)
        button_close.place(x=20, y=550)
        def share_capsule():
            t = Toplevel()
            t.title("Share Capsule Contents")
            t.geometry("900x900")
            t.iconbitmap("hourglass.ico")
            c61= Canvas(t, width=t.winfo_screenwidth(), height=t.winfo_screenheight())
            c61.pack(fill="both", expand=True)
            c61.create_text(750, 70, text=" Share Virtual Time Capsule ",font=("sans-serif", 15, "bold"))

            def email():
                share_url=f"https://mail.google.com"
                webbrowser.open(share_url)
            c61.create_text(690, 140, text="Share wih Gmail", font=("Times New Roman", 13)) 
            Button(t,text="Gmail",command=email,font=("Times New Roman",8,"")).place(x=800,y=130)

            def insta():
                insta_url=f"https://www.instagram.com" 
                webbrowser.open(insta_url)
            c61.create_text(700, 210, text="Share wih Instagram", font=("Times New Roman", 13))
            Button(t,text="Instagram",command=insta,font=("Times New Roman",8,"")).place(x=800,y=200)

            def face():
                face_url=f" https://www.facebook.com"
                webbrowser.open(face_url)
            c61.create_text(700, 280, text="Share wih FaceBook", font=("Times New Roman", 13)) 
            Button(t,text="Facebook",command=face,font=("Times New Roman",8,"")).place(x=800,y=270)

            def twi():
                twitter_url=f"https://twitter.com"
        
                webbrowser.open(twitter_url)
            c61.create_text(690, 350, text="Share wih Twitter",font=("Times New Roman", 13)) 
            Button(t,text="Twitter",command=twi,font=("Times New Roman",8,"")).place(x=800,y=340)
            
            def whats():
                whatsapp_url=f"https://web.whatsapp.com/"
                webbrowser.open(whatsapp_url)
            c61.create_text(700, 420, text="Share wih WhatsApp",font=("Times New Roman", 13)) 
            Button(t,text="Whatsapp",command=whats,font=("Times New Roman",8,"")).place(x=800,y=410)
        share = Button(top, text="Share", command=share_capsule)
        share.place(x=50, y=550)


    # Event name and date input
    c6.create_text(190, 220, text="Event Name:", font=("Times New Roman", 15, "bold"), fill="white")
    event_name_entry = Entry(top5, textvariable=event_name, width=40)
    event_name_entry.place(x=350, y=207)

    # Event date and time input
    c6.create_text(220, 290, text="Event Date and Time\n(yyyy-mm-dd hh:mm):", font=("Times New Roman", 15, "bold"), fill="white")
    event_date_entry = Entry(top5, textvariable=event_date, width=40)
    event_date_entry.place(x=350, y=290)

    # Message input
    c6.create_text(190, 360, text="Your Message:", font=("Times New Roman", 15, "bold"), fill="white")
    message_entry = Text(top5, width=40, height=4)
    message_entry.place(x=350, y=350)

    # Button to add message
    Button(top5, text="Add Message", font=("Times New Roman", 8, ""),
           command=lambda: add_message(message_entry)).place(x=700, y=360)

    # Button to upload image
    c6.create_text(188, 485, text="Upload Image:", font=("Times New Roman", 15, "bold"), fill="white")
    Button(top5, text="Upload Image", command=upload_image, font=("Times New Roman", 8, "")).place(x=345, y=470)
    # Display selected image
    image_label = Label(top5)
    image_label.place(x=470, y=465)

    # Button to record voice message
    c6.create_text(224, 540, text="Record Voice Message:", font=("Times New Roman", 15, "bold"), fill="white")
    Button(top5, text="Record", command=record_voice_message, font=("Times New Roman", 8, "")).place(x=350, y=530)

    # Button to upload video
    c6.create_text(185, 600, text="Upload Video:", font=("Times New Roman", 15, "bold"), fill="white")
    Button(top5, text="Upload Video", command=upload_video, font=("Times New Roman", 8, "")).place(x=350, y=590)

    # Button to start a time capsule opening party (e.g., video conference link)
    c6.create_text(200, 650, text="Video conference party:", font=("Times New Roman", 15, "bold"), fill="white")
    Button(top5, text="Start Party", command=start_capsule_party, font=("Times New Roman", 8, "")).place(x=350, y=640)

    # Button to save capsule data
    Button(top5, text="Save Capsule", font=("Times New Roman", 8, ""),
           command=save_capsule).place(x=700, y=720)

    # Button for "Must Open" functionality (force open capsule)
    Button(top5, text="Open Capsule", font=("Times New Roman", 8, ""),
           command=must_open_capsule).place(x=700, y=760)
    top5.mainloop()



import datetime
def travel():

    top6 = Toplevel()
    top6.title("Travel Capsule")
    top6.config(bg="Lavender")
    top6.iconbitmap("hourglass.ico")
    
    img1 = Image.open("travel.jpg")
    bgphoto1 = ImageTk.PhotoImage(img1.resize((top6.winfo_screenwidth(), top6.winfo_screenheight())))
    
    c6 = Canvas(top6, width=top6.winfo_screenwidth(), height=top6.winfo_screenheight())
    c6.pack(fill="both", expand=True)
    c6.create_image(0, 0, image=bgphoto1, anchor="nw")

    c6.create_text(650, 20, text="Virtual Time Capsule", font=("Segoe Script", 20, "bold"), fill="#FFC107", justify=CENTER)
    c6.create_text(645, 70, text="Virtual Time Capsule for Future Journeys", width=1300, font=("sans-serif", 15, "bold"), justify=CENTER)
    t31 = """Track Your Travel Dreams: A Capsule for Future Journeys
    This Travel Time Capsule helps you document your travel dreams, plans, and experiences. Capture your aspirations for new destinations and set dates for future adventures. Unlock your memories in the years to come and see where you’ve traveled."""
    c6.create_text(710, 130, text=t31, width=1400, font=("Times New Roman", 15), justify=LEFT)

    # Function to save goals (including travel goal) to a text file with a future date
    def save_goals():
        Goal = goal_entry.get()  # The goal entered by the user
        travel_goal = travel_goal_entry.get()  # The travel goal entered by the user
        future_date1 = future_date_entry.get()  # The future date entered by the user

        # Validate the input date format
        try:
            # Attempt to convert the input date into a datetime object
            future_date = datetime.datetime.strptime(future_date1, "%Y-%m-%d")
        except ValueError:
            # If the input doesn't match the expected format, show an error message
            messagebox.showerror("Invalid Date", "Please enter a valid date in the format YYYY-MM-DD")
            return

        # Get current date
        current_date = datetime.datetime.now()

        # Ensure the future date is later than the current date
        if future_date <= current_date:
            messagebox.showerror("Invalid Date", "The future date must be later than the current date.")
            return

        # If no travel goal is provided, set it to a default message
        if not travel_goal:
            travel_goal = "No travel goal specified."

        # Save the goal, travel goal, and date to a file
        with open("time_capsule.txt", "a") as file:
            file.write(f"Goal: {Goal}\nTravel Goal: {travel_goal}\nDate to be opened: {future_date.strftime('%Y-%m-%d')}\n\n")
        
        # Show success message after saving
        messagebox.showinfo("Success", "Your goal and travel goal have been saved to your time capsule!")

    # Function to display the current goals (including travel goal) in a Toplevel window
    def display_goals():
        try:
            with open("time_capsule.txt", "r") as file:
                contents = file.read()
                if contents:
                    # Create a new Toplevel window to show the contents
                    top = Toplevel()
                    top.title("Time Capsule Contents")
                    top.geometry("400x300")
                    top.iconbitmap("hourglass.ico")

                    # Create a scrollbar and a Text widget for displaying the contents
                    scrollbar = Scrollbar(top)
                    scrollbar.pack(side=RIGHT, fill=Y)

                    text_box = Text(top, wrap=WORD, width=50, height=15)
                    text_box.pack(pady=10)
                    text_box.insert(END, contents)
                    text_box.config(state=DISABLED)  # Make the text box read-only

                    # Attach the scrollbar to the text box
                    scrollbar.config(command=text_box.yview)
                    text_box.config(yscrollcommand=scrollbar.set)
                    def share_capsule():
                        t = Toplevel()
                        t.title("Share Capsule Contents")
                        t.geometry("900x900")
                        t.iconbitmap("hourglass.ico")
                        c61= Canvas(t, width=t.winfo_screenwidth(), height=t.winfo_screenheight())
                        c61.pack(fill="both", expand=True)
                        c61.create_text(750, 70, text=" Share Virtual Time Capsule ",font=("sans-serif", 15, "bold"))

                        def email():
                            share_url=f"https://mail.google.com"
                            webbrowser.open(share_url)
                        c61.create_text(690, 140, text="Share wih Gmail", font=("Times New Roman", 13)) 
                        Button(t,text="Gmail",command=email,font=("Times New Roman",8,"")).place(x=800,y=130)

                        def insta():
                            insta_url=f"https://www.instagram.com" 
                            webbrowser.open(insta_url)
                        c61.create_text(700, 210, text="Share wih Instagram", font=("Times New Roman", 13))
                        Button(t,text="Instagram",command=insta,font=("Times New Roman",8,"")).place(x=800,y=200)

                        def face():
                            face_url=f" https://www.facebook.com"
                            webbrowser.open(face_url)
                        c61.create_text(700, 280, text="Share wih FaceBook", font=("Times New Roman", 13)) 
                        Button(t,text="Facebook",command=face,font=("Times New Roman",8,"")).place(x=800,y=270)

                        def twi():
                            twitter_url=f"https://twitter.com"
                    
                            webbrowser.open(twitter_url)
                        c61.create_text(690, 350, text="Share wih Twitter",font=("Times New Roman", 13)) 
                        Button(t,text="Twitter",command=twi,font=("Times New Roman",8,"")).place(x=800,y=340)
                        
                        def whats():
                            whatsapp_url=f"https://web.whatsapp.com/"
                            webbrowser.open(whatsapp_url)
                        c61.create_text(700, 420, text="Share wih WhatsApp",font=("Times New Roman", 13)) 
                        Button(t,text="Whatsapp",command=whats,font=("Times New Roman",8,"")).place(x=800,y=410)

                    share = Button(top, text="Share", command=share_capsule)
                    share.place(x=40, y=550)
    
                else:
                    messagebox.showinfo("Time Capsule Contents", "Your time capsule is empty!")
        except FileNotFoundError:
            messagebox.showinfo("Time Capsule Contents", "No goals saved yet. Start adding them!")
    
    



    # Function to open Google Maps in the default web browser
    def show_map():
        location = travel_goal_entry.get()

        if not location:
            messagebox.showerror("Missing Information", "Please enter a travel goal (destination).")
            return

        # Create Google Maps URL
        map_url = f"https://www.google.com/maps?q={location.replace(' ', '+')}"

        # Open the map in the default web browser
        webbrowser.open(map_url)

    # Function to open the time capsule if the current date matches the future date
    def open_capsule():
        try:
            with open("time_capsule.txt", "r") as file:
                contents = file.readlines()
                if contents:
                    # Iterate through each entry in the file
                    for i in range(len(contents)-1, -1, -1):  # Read from the end of the file
                        line = contents[i].strip()

                        if line.startswith("Date to be opened:"):
                            future_date_str = line.split(": ")[1]

                            # Convert the saved future date to datetime object
                            try:
                                future_date = datetime.datetime.strptime(future_date_str, "%Y-%m-%d")
                            except ValueError:
                                messagebox.showerror("Invalid Date Format", "The saved future date format is invalid.")
                                return

                            current_date = datetime.datetime.now()

                            if current_date >= future_date:
                                # If the date has arrived, display the goals
                                display_goals()
                                return
                            else:
                                messagebox.showerror("Time Capsule", "The capsule is not yet open. The set date hasn't arrived.")
                                return

                    messagebox.showinfo("Time Capsule", "No valid time capsule entry found.")
                else:
                    messagebox.showinfo("Time Capsule", "Your time capsule is empty!")
        except FileNotFoundError:
            messagebox.showinfo("Time Capsule", "No goals saved yet. Start adding them!")
    

 # Labels and Entries for the form
    c6.create_text(450, 250, text="Enter your Name:", font=("sans-serif", 15, ""), justify=CENTER)
    name_entry = Entry(top6, width=30)  # Changed variable name to 'name_entry'
    name_entry.place(x=610, y=242)

    c6.create_text(480, 320, text="Enter your goal or dream:", font=("sans-serif", 15, ""), justify=CENTER)
    goal_entry = Entry(top6, width=50)  # Kept this as 'goal_entry' for goal/dream
    goal_entry.place(x=610, y=300)

    c6.create_text(458, 430, text="Enter your travel goal\n(e.g., place to visit):", font=("sans-serif", 15, ""))
    travel_goal_entry = Entry(top6, width=30)
    travel_goal_entry.place(x=610, y=430)

    # Button to show map of the travel goal
    map_button = Button(top6, text="Google Map", command=show_map)
    map_button.place(x=820, y=425)

    c6.create_text(460, 510, text="Enter the date to open\n(YYYY-MM-DD):", font=("sans-serif", 15, ""))
    future_date_entry = Entry(top6, width=30)
    future_date_entry.place(x=610, y=490)

    # Buttons to save and display goals
    save_button = Button(top6, text="Save Goal", command=save_goals)
    save_button.place(x=610, y=570)

    view_button = Button(top6, text="View Goal", command=display_goals)
    view_button.place(x=680, y=570)

    # Open Capsule Button to check the current date against the saved future date
    open_capsule_button = Button(top6, text="Open Capsule", command=open_capsule)
    open_capsule_button.place(x=780, y=570)

    top6.mainloop()
travel()



root.mainloop()