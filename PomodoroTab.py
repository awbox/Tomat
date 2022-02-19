import time_utils
from tkinter import *

class PomodoroTab:
    def __init__(self, name, root, duration, background_image):
        self.name = name
        self.root = root
        self.duration_sec = time_utils.time_in_seconds(duration)

        self.background = Canvas(self.root, width=300, height=300)
        self.background.pack(fill="both", expand=True)
        self.background.create_image(0, 0, image=background_image, anchor="nw")

        self.timer_running = False
        self.create_timer_text()
        self.create_buttons()

    def create_timer_text(self):
        self.timer_text = self.background.create_text(150, 150, text=time_utils.time_display_format(self.duration_sec),
                                                      fill='black', font=("Courier", 55, "bold"))

    def update_time(self, current_time):
        self.background.itemconfig(self.timer_text, text=current_time)

    def pomodoro_timer(self):
        for current_time in time_utils.count_down(self.duration_sec):
            self.update_time(current_time)
            self.root.update()
            self.root.after(1000)
            if not self.timer_running:
                self.current_time = current_time
                break

    def start_timer(self):
        self.timer_running = True
        self.pomodoro_timer()

    def stop_timer(self):
        self.timer_running = False

    def create_buttons(self):
        self.start_button = Button(self.background, text="start", command=self.start_timer)
        self.background.create_window(10, 10, anchor="nw", window=self.start_button)

        self.stop_button = Button(self.background, text="stop", command=self.stop_timer)
        self.background.create_window(200, 10, anchor="nw", window=self.stop_button)

