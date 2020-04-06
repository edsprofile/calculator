from tkinter import Tk, Label, Button, LEFT, RIGHT, W

class FirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("GUI")

        self.label = Label(master, text='This is our first GUI!')
        self.label.grid(columnspan=2, sticky=W)

        self.greet_button = Button(master, text='Greet', command=self.greet)
        self.greet_button.grid(row=1)

        self.close_button = Button(master, text='Close', command=master.quit)
        self.close_button.grid(row=1, column=1)

    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = FirstGUI(root)
root.mainloop()
