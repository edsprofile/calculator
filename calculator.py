from tkinter import Tk, Label, Button, LEFT, RIGHT, N, E, S, W, IntVar

class CalculatorGUI:
    DISPLAY_TEXT = [
            '0',
            '1',
            '2',
            '3',
            '4',
            '5'
        ]
    def __init__(self, master):
        self.master = master
        master.title("CalculatorGUI")

        self.label_index = 0;

        self.label = Label(master, text="Display", borderwidth=2,
                           relief='solid', anchor=E, padx=5, pady=5)
        self.label.grid(columnspan=4, sticky=W+E, column=0, padx=2, pady=2)

        self.one_button = Button(master, text='1', command=self.greet)
        self.one_button.grid(row=1)

        self.two_button = Button(master, text='2', command=self.greet)
        self.two_button.grid(row=1,column=1)

        self.three_button = Button(master, text='3', command=self.greet)
        self.three_button.grid(row=1,column=2)

        self.four_button = Button(master, text='4', command=self.greet)
        self.four_button.grid(row=2)

        self.five_button = Button(master, text='5', command=self.greet)
        self.five_button.grid(row=2,column=1)

        self.six_button = Button(master, text='6', command=self.greet)
        self.six_button.grid(row=2,column=2)

        self.seven_button = Button(master, text='7', command=self.greet)
        self.seven_button.grid(row=3)

        self.eight_button = Button(master, text='8', command=self.greet)
        self.eight_button.grid(row=3,column=1)

        self.nine_button = Button(master, text='9', command=self.greet)
        self.nine_button.grid(row=3,column=2)

        self.zero_button = Button(master, text='0', command=root.destroy)
        self.zero_button.grid(row=4, column=1)

        self.divide_button = Button(master, text='/', command=root.destroy)
        self.divide_button.grid(row=1, column=3)

        self.multiply_button = Button(master, text='*', command=root.destroy)
        self.multiply_button.grid(row=2, column=3)

        self.subtract_button = Button(master, text='-', command=root.destroy)
        self.subtract_button.grid(row=3, column=3)

        self.add_button = Button(master, text='+', command=root.destroy)
        self.add_button.grid(row=4, column=3)

        self.equal_button = Button(master, text="=", command=self.greet)
        self.equal_button.grid(row=5, column=3)

        self.close_button = Button(master, text='Close', command=root.destroy)
        self.close_button.grid(row=5, column=1)

    def greet(self):
        print("Greetings!")

    def cycle_label_text(self, event):
        self.label_index +=1
        self.label_index %= len(self.DISPLAY_TEXT)
        self.label_text.set(self.DISPLAY_TEXT[self.label_index])


root = Tk()
my_gui = CalculatorGUI(root)
root.mainloop()
