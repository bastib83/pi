from tkinter import *

window = Tk()

window.title("Basti´s PyGUI")

lbl = Label(window, text="Yo Ko, bÄM!", font=("Arial Bold", 50))

lbl.grid(column=0, row=0)

window.geometry('350x200')


window.mainloop()
