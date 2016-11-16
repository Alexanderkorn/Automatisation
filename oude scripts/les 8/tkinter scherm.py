__author__ = 'alexander'
from tkinter import *
from tkinter.messagebox import showinfo
def antwoord(text):
    showinfo(title='popup', message='Hoi '+text)
window = Tk()
lable = Label(window, text='Hello World')
lable.pack()

naam = Entry(window)
naam.pack()

button = Button(window, text='Klik hier!', command=(lambda: antwoord(naam.get())))
button.pack()




window.mainloop()