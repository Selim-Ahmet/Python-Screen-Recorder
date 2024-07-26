from tkinter import *
import pyscreenrec

# Initialize the root window
root = Tk()
root.geometry("400x600")
root.resizable(False, False)
root.title("Screen Recorder")
root.config(bg="#fff")

# Initialize the screen recorder
rec = pyscreenrec.ScreenRecorder()

def start_rec():
    file = Filename.get()
    rec.start_recording(str(file + ".mp4"))

def pause_rec():
    rec.pause_recording()

def resume_rec():
    rec.resume_recording()

def stop_rec():
    rec.stop_recording()

# Load icons and background images
image_icon = PhotoImage(file="icon.png")
root.iconphoto(False, image_icon)

bg1 = PhotoImage(file="background 1.png")
Label(root, image=bg1, bg="#fff").place(x=0, y=35)
bg2 = PhotoImage(file="background 2.png")
Label(root, image=bg2, bg="#fff").place(x=180, y=370)

lbl = Label(root, text="Screen Recorder", bg="#fff", font="arial 15 bold")
lbl.pack(pady=20)

image3 = PhotoImage(file="record_2.png")
Label(root, image=image3, bd=0).pack(pady=30)

Filename = StringVar()
entry = Entry(root, textvariable=Filename, width=18, font="arial 15")
entry.place(x=100, y=350)
Filename.set("recording")

start = Button(root, text="Start", font="arial 18", bd=0, command=start_rec)
start.place(x=160, y=189)

image4 = PhotoImage(file="play2.png")
play = Button(root, image=image4, bd=0, bg="#fff", command=pause_rec)
play.place(x=40, y=450)

image5 = PhotoImage(file="pause.png")
resume = Button(root, image=image5, bd=0, bg="#fff", command=resume_rec)
resume.place(x=150, y=450)

image6 = PhotoImage(file="stop.png")
stop = Button(root, image=image6, bd=0, bg="#fff", command=stop_rec)
stop.place(x=250, y=450)

# Run the Tkinter main loop
root.mainloop()
