from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import math
import time
# ---------------------------- ZMIENNE/STAŁE ------------------------------- #
# <W TYM MIEJSCU DODAJ 4 STAŁE Z DOWOLNYMI KOLORAMI DO UI>
WORK_IMAGE = "Tomat_images/1.jpg"
SHORT_BREAK_IMAGE = "Tomat_images/2.jpg"
LONG_BREAK_IMAGE = "Tomat_images/3.jpg"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
mark = ''

# ---------------------------- TIMER RESTART --------------------------- #
def reset_timer():
    pass


# ---------------------------- TIMER CALCULATIONS ------------------------- #
def start_timer(duration):
    pass




# ---------------------------- COUNTDOWN CALCULATIONS --------------------------- #

def count_down(count, timer_object):
    timer_object['text'] = f"{count:02d}:00"
    timer_object.pack()
    timer_object.place(anchor=CENTER, relx=0.5, rely=0.5)
    root.update()
    time.sleep(1)
    while count:
        count -= 1
        for sec in range(59, -1, -1):
            timer_object['text'] = f"{count:02d}:{sec:02d}"
            timer_object.pack()
            timer_object.place(anchor=CENTER, relx=0.5, rely=0.5)
            root.update()
            time.sleep(1)
            sec -= 1

root = Tk()
root.geometry("300x300")
root.title('Tomat')

tabs_window = ttk.Notebook(root, width=300, height=300)
tabs_window.grid()

work_image = ImageTk.PhotoImage(file=WORK_IMAGE)
short_break_image = ImageTk.PhotoImage(file=SHORT_BREAK_IMAGE)
long_break_image = ImageTk.PhotoImage(file=LONG_BREAK_IMAGE)


work_tab = Canvas(tabs_window, width=300, height=300)
work_tab.pack(fill="both", expand=True)
work_tab.create_image(0, 0, image=work_image, anchor="nw")
timer_text = Label(work_tab, text="25:00", anchor='center', font=(FONT_NAME, 35, "bold"))
timer_text.pack(expand=True)
timer_text.place(anchor=CENTER, relx=0.5, rely=0.5)

short_break_tab = Canvas(tabs_window, width=300, height=300)
short_break_tab.pack(fill="both", expand=True)
short_break_tab.create_image(0, 0, image=short_break_image, anchor="nw")
break_timer_text = Label(short_break_tab, text="05:00", anchor='center', font=(FONT_NAME, 35, "bold"))
break_timer_text.pack(expand=True)
break_timer_text.place(anchor=CENTER, relx=0.5, rely=0.5)

long_break_tab = Canvas(tabs_window, width=300, height=300)
long_break_tab.pack(fill="both", expand=True)
long_break_tab.create_image(0, 0, image=long_break_image, anchor="nw")
long_break_timer_text = Label(long_break_tab, text="20:00", anchor='center', font=(FONT_NAME, 35, "bold"))
long_break_timer_text.pack(expand=True)
long_break_timer_text.place(anchor=CENTER, relx=0.5, rely=0.5)

start_button = Button(work_tab, text="start", command=(lambda: count_down(WORK_MIN, timer_text)))
work_tab.create_window(10, 10, anchor="nw", window=start_button)
restart_button = Button(work_tab, text="restart", command=(lambda: count_down(WORK_MIN, timer_text)))
work_tab.create_window(200, 10, anchor="nw", window=restart_button)

break_start_button = Button(short_break_tab, text="start", command=(lambda: count_down(SHORT_BREAK_MIN, break_timer_text)))
short_break_tab.create_window(10, 10, anchor="nw", window=break_start_button)
break_restart_button = Button(short_break_tab, text="restart", command=(lambda: count_down(SHORT_BREAK_MIN, break_timer_text)))
short_break_tab.create_window(200, 10, anchor="nw", window=break_restart_button)

long_break_start_button = Button(long_break_tab, text="start", command=(lambda: count_down(LONG_BREAK_MIN, long_break_timer_text)))
long_break_tab.create_window(10, 10, anchor="nw", window=long_break_start_button)
long_break_restart_button = Button(long_break_tab, text="restart", command=(lambda: count_down(LONG_BREAK_MIN, long_break_timer_text)))
long_break_tab.create_window(200, 10, anchor="nw", window=long_break_restart_button)

tabs_window.add(work_tab, text="Szychta")
tabs_window.add(short_break_tab, text="Dechnij Se")
tabs_window.add(long_break_tab, text="Fajrant")

root.wm_attributes('-transparent', False)
root.mainloop()
