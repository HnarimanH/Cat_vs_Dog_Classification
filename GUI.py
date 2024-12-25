from tkinter import *


class Gui:
    def __init__(self):
        self.root = Tk()
        self.root.attributes('-fullscreen',True)
        self.root.title("Cat_vs_dog")
        self.label = Label(self.root,text="hi")
        self.root.mainloop()
        
app = Gui()