# Python Tkinter GUI Based 'Love Calculator'
from tkinter import *
import random
# Creating GUI Window
root = Tk()
root.geometry('400x240')
root.title('Love Calculator...❤️')

# Function to Calculate Love Percentage
def calculate_love():
    # Value Will Contain Digits Between 0-9
    st = '0123456789'
    # Result Will be in Double Digits
    digit = 2
    temp = " ".join(random.sample(st, digit))
    result.config(text=temp)

# Heading on Top
heading = Label(root, text="Love Calculator(●'◡'●)")
heading.pack()

# Slot/Input for the First Name
slot1 = Label(root, text="Enter Your Name: ")
slot1.pack()
name1 = Entry(root, border=5)
name1.pack()

# Slot/Input for the Partner Name
slot2 = Label(root, text="Enter Your Partner Name: ")
slot2.pack()
name2 = Entry(root, border=5)
name2.pack()

# Create a Button and Place at a Particular
bt = Button(root, text="Calculate", height=1, width=7, command=calculate_love)
bt.pack()

# Text on Result Slot
result = Label(root, text='Love Percentage Between Both of You:')
result.pack()

# Starting the GUI
root.mainloop()
