import ImageTk
import PIL.Image
from Tkinter import *
from tkMessageBox import *


class UI:

    def __init__(self):
        self.master = Tk()
        self.master.title("Password Check")

        # set size
        self.master.minsize(80, 60)
        self.master.geometry("320x100")

        # To center the window
        self.master.update_idletasks()
        width = self.master.winfo_width()
        frm_width = self.master.winfo_rootx() - self.master.winfo_x()
        win_width = width + 2 * frm_width
        height = self.master.winfo_height()
        titlebar_height = self.master.winfo_rooty() - self.master.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = self.master.winfo_screenwidth() // 2 - win_width // 2
        y = self.master.winfo_screenheight() // 2 - win_height // 2
        self.master.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.master.deiconify()

        # add text box
        Label(self.master, text="Enter password").grid(row=0)

        self.e1 = Entry(self.master)
        self.e1.grid(row=0, column=1)

        # add buttons
        Button(self.master, text='Quit', command=self.master.quit).grid(row=3, column=0, sticky=W, pady=4)
        Button(self.master, text='Check', command=self.__show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

    def __show_entry_fields(self):
        print("Entered password: %s" % (self.e1.get()))
        ip = self.e1.get()

        with open("../data/all") as file:
            data = file.read().splitlines()

        if ip in data:
            print "failure"
            self.__failure()
        else:
            print "success"
            self.__success()

    def render(self):
        mainloop( )

    def __failure(self):
        window = Toplevel()
        window.title("Password Check")
        window.geometry("610x380")
        window.configure(background='grey')

        # To center the window
        window.update_idletasks()
        width = window.winfo_width()
        frm_width = window.winfo_rootx() - window.winfo_x()
        win_width = width + 2 * frm_width
        height = window.winfo_height()
        titlebar_height = window.winfo_rooty() - window.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = window.winfo_screenwidth() // 2 - win_width // 2
        y = window.winfo_screenheight() // 2 - win_height // 2
        window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        window.deiconify()

        path = "../data/pic.png"

        # Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
        img = ImageTk.PhotoImage(PIL.Image.open(path))

        # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
        panel = Label(window, image=img)

        # The Pack geometry manager packs widgets in rows or columns.
        panel.pack(side="top")

        button = Button(window, text='Ok', command=window.destroy)
        button.pack(side="bottom")

        # Start the GUI
        window.mainloop()

    def __success(self):
        showinfo("Password Check", "Success! Password is safe from dictionary attack!")