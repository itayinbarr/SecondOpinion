from front import MyWindow
from tkinter import *

# Run this file to start the software
# ---------------------------

# Introduction
print("***************************")
print("***************************")
print("***************************")
print("Welcome to SecondOpinion - A dense neural network model I trained, to recognize 3 types of brain tumors.")
print("---------------------------")
print("I recommend storing the photos in ./patients")
print("---------------------------")

# You can use the input to load 1 or multiple windows
print("Type down the number of machine windows to open. When finished, press Enter")
numberOfWindows = int(input())
for i in range(numberOfWindows):
    window = Tk()
    mywin = MyWindow(window)
    window.title('SecondOpinion Machine')
    window.geometry("600x350")

window.mainloop()
