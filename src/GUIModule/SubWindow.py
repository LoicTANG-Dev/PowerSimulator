import tkinter
from Common import Observer

class SubWindow(Observer.Observer):

    win = None

    def __init__(self):
        self.win = tkinter.Toplevel()

    def show(self):
        self.win.mainloop(0)
    
    def listen(self):
        return