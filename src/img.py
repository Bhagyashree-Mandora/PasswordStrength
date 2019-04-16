import Tkinter as tk
from PIL import ImageTk, Image
from tkMessageBox import *


# This creates the main window of an application
window = tk.Toplevel()
window.title("Password Check")
window.geometry("500x500")
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

path = "../data/pic3.jpg"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "top")#, fill = "both", expand = "yes")

button = tk.Button(window, text='Ok', command=window.quit)
button.pack(side = "bottom")#, fill = "both", expand = "yes")

#Start the GUI
window.mainloop()