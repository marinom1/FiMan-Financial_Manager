from tkinter import *
from tkinter.ttk import *

# GUI Container
container = Tk()
container.configure(bg='#2c2c2e')

# Frames

# Top Frame
topFrame = Frame(container)
topFrame.pack(side=TOP)

# Bottom Frame
bottomFrame = Frame(container)
bottomFrame.pack(side=BOTTOM)

"""
# Navbar Frame
navBar = Frame(topFrame)
navBar.pack()
"""

"""
# Buttons
button1 = Button(topFrame, text='BUTTON 1', bg='#2c2c2e', fg='white', font='Roboto 10 bold')
button2 = Button(bottomFrame, text='BUTTON 2', bg='#2c2c2e', fg='white', font='Roboto 10 bold')

button1.pack()
button2.pack()
"""

container.geometry('852x480')

container.mainloop()