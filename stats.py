from tkinter import *
#import input as inp


def popupmsg():
    popup = Tk()
    popup.geometry("250x100")
    popup.wm_title("Confirm")
    label = Label(popup, text = "Do you want to Restart")
    label.pack(side = "top", fill = "x", pady = 10)
    B1 = Button(popup, text = "OK", command = popup.destroy,  width = "20", height = "2")
    B1.pack()
    popup.mainloop()








screen =Tk()

screen.geometry("500x500")
screen.title("Sleep Detection System")

heading = Label(text = "Journey Statistics", bg = "grey", fg = "white", width = "500", height = "3")
heading.config(font=("Courier", 14))

heading.pack()    

#name_label = Label(text = inp.name)

name_label = Label(text = "Driver's Name : Priyanka")
name_label.config(font=("Arial", 10))

duration_label = Label(text = "Journey Duration : 165 min")
duration_label.config(font=("Arial", 10))

sleep_label = Label(text = "No. of times Driver felt drowsiness : 8")
sleep_label.config(font=("Arial", 10))

name_label.place(x = 20, y = 100)
duration_label.place(x = 20, y = 135)
sleep_label.place(x = 20, y = 170)


start = Button(screen, text = "Restart", width = "15", height = "2", command = popupmsg)
start.place(x = 20, y = 260)

end = Button(screen, text = "Quit", width = "15", height = "2", command = screen.destroy)
end.place(x = 180, y = 260)

