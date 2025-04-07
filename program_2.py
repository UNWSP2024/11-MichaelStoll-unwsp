#title:Show info
#author: michael stoll
#date:4/7/2025
import tkinter
import tkinter.messagebox
class GUI:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title('Window')

        self.button = tkinter.Button(self.window, text='Show Info', command=self.action1)
        self.button.pack(pady=20)

        self.gui_quit = tkinter.Button(self.window, text='Quit', command=self.window.destroy)
        self.gui_quit.pack(pady=20)

        tkinter.mainloop()
    @staticmethod
    def action1():
        tkinter.messagebox.showinfo('Information', 'Name: Michael Stoll '
                                    '\nAddress (fictional): 1234 5th st Duluth, Minnesota, 55287')


my_gui = GUI()
