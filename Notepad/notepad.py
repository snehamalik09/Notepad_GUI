#Notepad GUI
#Author- Sneha Malik
#Date- Oct-2021

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def cut():
    textarea.event_generate(("<<Cut>>"))


def copy():
    textarea.event_generate(("<<Copy>>"))


def paste():
    textarea.event_generate(("<<Paste>>"))


def about():
    messagebox.showinfo("Notepad", "Notepad by Sneha!")


def Newfile():
    global file
    root.title("Untitled - Notepad")
    textarea.delete(1.0,END)


def Savefile():
    global file
    if file == None:
        # save as new file
        file = asksaveasfilename(initialfile='Untitled.txt',
                                 defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])

        if file == "":
            file = None
        else:

            # try to save the file
            file = open(file, "w")
            file.write(textarea.get(1.0, END))
            file.close()
            # change the window title
            root.title(os.path.basename(file) + " - Notepad")


    else:
        file = open(file, "w")
        file.write(textarea.get(1.0, END))
        file.close()


def Openfile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Document", "*.txt")])

    # no file to open
    if file == "":
        file = None
    else:
        # Try to open the file
        # change the window title
        root.title(os.path.basename(file) + " - Notepad")
        textarea.delete(1.0, END)
        f = open(file, "r")
        textarea.insert(1.0, f.read())
        f.close()


if __name__=='__main__':
    # Basic tkinter setup
    root=Tk()
    root.geometry("1000x470")
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("notepad.ico")

    file=None

    #Add textarea
    textarea=Text(root, font="lucida 10 ")
    textarea.pack(expand=True, fill="both")

    #Lets's Create Menu Bar
    mainmenu=Menu(root)
    Filemenu=Menu(mainmenu, tearoff=0)
    #To open new file
    Filemenu.add_command(label="New", command=Newfile)

    # To save the current file
    Filemenu.add_command(label="Save", command=Savefile)

    # To open already exisitng file
    Filemenu.add_command(label="Open", command=Openfile)

    Filemenu.add_separator()

    # To terminate
    Filemenu.add_command(label="Exit", command=root.destroy)

    #Adding cascade to File menu
    mainmenu.add_cascade(label="File", menu=Filemenu)

    Editmenu=Menu(mainmenu, tearoff=0)
    # To give a feature of cut
    Editmenu.add_command(label="cut", command=cut)

    # To give a feature of copy
    Editmenu.add_command(label="copy", command=copy)

    # To give a feature of paste
    Editmenu.add_command(label="paste", command=paste)

    # To give a feature of editing
    mainmenu.add_cascade(label="Edit", menu=Editmenu)

    # To create a feature of description of the notepad
    Helpmenu=Menu(mainmenu, tearoff=0)
    Helpmenu.add_command(label="About", command=about)
    mainmenu.add_cascade(label="Help", menu=Helpmenu)
    root.config(menu=mainmenu)

    #Adding scrollbar to the notepad
    scroll=Scrollbar(textarea)
    scroll.pack(anchor="ne", side="right", fill="y")
    scroll.config(command=textarea.yview)
    textarea.config(yscrollcommand=scroll.set)

    # Run main application
    root.mainloop()


