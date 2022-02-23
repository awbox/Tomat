# --------------------------- standard lib imports ---------------------------
from tkinter import Tk
from tkinter.ttk import Notebook
from PIL import ImageTk

# --------------------------- project imports ---------------------------
from TabObject import TabObject

# --------------------------- constants ---------------------------
WORK_IMAGE = "Tomat_images/1.jpg"
SHORT_BREAK_IMAGE = "Tomat_images/2.jpg"
LONG_BREAK_IMAGE = "Tomat_images/3.jpg"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ----------------- Initalizing root window and Notebook widget -----------
root = Tk()
root.geometry("300x300")
root.title('Tomat')

tabs_window = Notebook(root, width=300, height=300)
tabs_window.pack()

# --------------------------- Initializing tabs ---------------------------
work_image = ImageTk.PhotoImage(file=WORK_IMAGE)
work_tab = TabObject("work", root, WORK_MIN, work_image)

short_break_image = ImageTk.PhotoImage(file=SHORT_BREAK_IMAGE)
short_break_tab = TabObject("short break", root, SHORT_BREAK_MIN, short_break_image)

long_break_image = ImageTk.PhotoImage(file=LONG_BREAK_IMAGE)
long_break_tab = TabObject("long break", root, LONG_BREAK_MIN, long_break_image)


# --------------------------- adding tabs to Notebook widget ---------------------
tabs_window.add(work_tab.background, text="Szychta")
tabs_window.add(short_break_tab.background, text="Dechnij Se")
tabs_window.add(long_break_tab.background, text="Fajrant")

# ------------------- executing tkinter mainloop ---------------------
root.mainloop()
