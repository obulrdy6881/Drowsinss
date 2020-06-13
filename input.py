from tkinter import *
import tkinter as tk
#custom functions
from Drowsiness_Detection import open
def save_info():

    name_info = name.get()
    duration_info = duration.get()
    
    duration_info = str(duration_info)
    
    file = open("details.txt", "a")

    file.write("Driver Name: ")
    file.write(name_info)

    file.write("\nDrive Duration: ")
    file.write(duration_info)
    file.write("\n\n\n\n")
    
    file.close()

    print("Hello! Mr.", name_info,", you can start your ride safely")



    

#window
screen = tk.Tk()

screen.geometry("500x500")
screen.title("Sleep Detection System")

heading = Label(text = "Enter Journey Details", bg = "grey", fg = "white", width = "500", height = "3")
heading.config(font=("Courier", 14))

heading.pack()    


name = StringVar()
duration = IntVar()

name_label =  tk.Label(text = "Driver's Name")
name_label.config(font=("Arial", 10))

duration_label =  tk.Label(text = "Journey Duration(min)")
duration_label.config(font=("Arial", 10))

name_input = Entry(textvariable = name, width = "40")
duration_input = Entry(textvariable = duration, width = "40")

name_label.place(x = 20, y = 100)
name_input.place(x = 20, y = 130)

duration_label.place(x = 20, y = 180)
duration_input.place(x = 20, y = 210)

#start = Button(text = "Start Now", width = "70", height = "2")
#start.place(x = 0, y = 440)

start = tk.Button(screen, text = "Start Now", width = "15", height = "2", command = open)
start.place(x = 20, y = 260)

end = tk.Button(screen, text = "Quit", width = "15", height = "2", command = screen.destroy)
end.place(x = 180, y = 260)
screen.mainloop()



if name_label != True or duration_label != True:
    popup = tk.Tk()
    popup.geometry("250x100")
    popup.wm_title("Missing")
    label = tk.Label(popup, text="Enter complete details")
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="OK", command=popup.destroy, width="20", height="2")
    B1.pack()
    popup.mainloop()