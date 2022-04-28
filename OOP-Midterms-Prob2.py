from tkinter import *
from tkinter import ttk
window = Tk()

window.title("Special Midterm Exam in OOP")
window.geometry("500x400")

# Insert button widget
lbl = Label(window,text = "Clicking the Button Changes the Color")
lbl.place(relx=.5,y=75, anchor="center")
btn = Button(window, text = "Click me!", fg="Black", activebackground="Yellow")
btn.place(x= 240, y=200, anchor="center")

window.mainloop()