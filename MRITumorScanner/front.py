from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from back import *
from PIL import ImageTk, Image


# Class of software window
# We can create as many windows as we wish
# You can create instances through runner.py
# ---------------------------
class MyWindow:
    def __init__(self, win):
        # Creating the visuals
        # ---------------------------
        # Labels
        self.lblTitle = Label(win, font="Helvetica 16 bold", text='Second Opinion - MRI Brain Tumor Scan')
        self.lblSubtitle = Label(win, text='Choose an MRI photo')
        self.lblResult = Label(win, font="Helvetica 14 bold", text='')
        self.lblAcc = Label(win, font="Helvetica 14 bold", text='')
        # Buttons
        self.btnOpenFile = Button(win, text='Load Photo', command=self.select_file)
        self.btnRawPlot = Button(win, text='Analyze It', command=self.process_file)
        # EEG file loaded by user
        # ---------------------------
        self.selectedFile = "No file loaded"
        self.savedFileName = "Untitled"
        # Placing the objects
        # ---------------------------
        # Labels
        self.lblTitle.place(x=20, y=50)
        self.lblSubtitle.place(x=20, y=90)
        self.lblResult.place(x=20, y=140)
        self.lblAcc.place(x=20, y=180)
        # Buttons
        self.btnOpenFile.place(x=170, y=90)
        self.btnRawPlot.place(x=270, y=90)

    # Triggered when Load File is pressed
    def select_file(self):
        # All file types working with the software
        filetypes = (
            #('set files', '*.set'),

        )
        self.selectedFile = askopenfilename(filetypes=filetypes, title='Open a file')
        if not self.selectedFile:
            # Error catcher
            messagebox.showerror("Bad File Loaded", "Bad File. Load Again")
        if self.selectedFile:
            # Printing to console that the file is successfully loaded to the software
            print("---------------------------------")
            print(f"{self.selectedFile.rsplit('/', 1)[-1].split('.')[0]}", "selected successfully, click "
                                                                           "Analyze to proceed.")

    def process_file(self):
        result = use_model(self.selectedFile)
        new_text = 'This MRI picture shows ' + result[0]
        percent = "With a {} percent confidence.".format(result[1])
        self.lblResult.config(text=new_text)
        self.lblAcc.config(text=percent)
