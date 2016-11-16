""""__author__ = 'alexander'
try:
    import tkinter
except:
    import Tkinter as tkinter

root = tkinter.Tk()

def grey(*args,**kwargs):
    root.configure(background="grey")

def bthing():
    root.configure(background="red")
    root.after(1000, grey)

tkinter.Button(text="OK", command=bthing).pack()

root.configure(background="grey")
root.geometry("400x400")

root.mainloop()

import time
import random
from tkinter import *

class GetClicktime():
    def __init__(self):
        self.j=0
        self.t=[]
        self.mgui=Tk()
        self.mgui.geometry('200x200')
        self.mgui.title('Queue System')
        self.st = Button(self.mgui, text="Next Customer", command = self.PrintNumber)
        self.st.pack()
        #self.st.bind('<Button-1>',callback)
        self.label = Label(self.mgui, text=str(self.j))
        self.label.pack()
        self.mgui.mainloop()

    def PrintNumber(self):
       self.j+=1
       self.label.config(text=str(self.j))
       print(self.j)
       t = (time.strftime("%H:%M:%S"))
       d = time.strftime("%d/%m/%Y")
       self.t.append(int(t.replace(':','')))
       print(self.t)
       if self.j >2:
           print('the time between clicks is:',self.t[self.j-1]-self.t[self.j-2],'seconds')
       print(t,d)
       return

if __name__ == "__main__":
    GetClicktime()
"""""
import pythoncom, pyHook
import timer
from copy import copy
from time import sleep
from threading import Timer

currentCounts = {}
countsToStore = {}

def onKeyDown(event):
    keyname = event.GetKey()
    if keyname not in currentCounts:
        currentCounts[keyname] = 1
    else:
        currentCounts[keyname] += 1

def storeCounts():
    while True:
        countsToStore = copy(currentCounts)
        wordlefile = open("keyswordle.txt", "w")
        print>>wordlefile, "key\tcount"
        for keyname in countsToStore:
            label = keyname
            if keyname.startswith("Media_"):
                label = keyname[6:]
            print>>wordlefile, label + "\t" + str(countsToStore[keyname])
        wordlefile.close()
        countsToStore = {}
        sleep(900)

captureThread = Timer(900.0, storeCounts)
captureThread.start()

hookmgr = pyHook.HookManager()
hookmgr.KeyDown = onKeyDown
hookmgr.HookKeyboard()
pythoncom.PumpMessages()