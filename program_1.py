#title:Favorite saying
#author: michael stoll
#date: 4/7/2025
import tkinter
class GUI:
    def __init__(self):
        self.window = tkinter.Tk()

        self.window.title('Window')
        self.label = tkinter.Label(self.window, text='Hello there', borderwidth=100, relief='sunken')
        self.label.pack(side='left')
        tkinter.mainloop()

my_gui = GUI()