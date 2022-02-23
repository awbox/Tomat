import time_utils
from tkinter import Canvas, Button


class TabObject:
    def __init__(self, name, root, duration, background_image):
        """
        Tab widget, containing image background, start/stop buttons, and count down timer display.
        To be used with tkinter Notebook as root widget.
        Uses tkinter.Canvas and tkinter.Button for object initialization.
        :param name: str, name of the object instance
        :param root: parent tkinter widget, Notebook object preferred
        :param duration: int, time duration for countdown
        :param background_image: ImageTk.PhotoImage object
        """
        self.name = name
        self.root = root
        self.duration_sec = time_utils.time_in_seconds(duration)

        self.background = Canvas(self.root, width=300, height=300)
        self.background.pack(fill="both", expand=True)
        self.background.create_image(0, 0, image=background_image, anchor="nw")

        self.timer_running = False
        self.create_timer_text()
        self.create_buttons()

    def create_timer_text(self) -> None:
        """
        Create timer display in widget center.
        :return: None
        """
        self.timer_text = self.background.create_text(150, 150, text=time_utils.time_display_format(self.duration_sec),
                                                      fill='black', font=("Courier", 55, "bold"))

    def create_buttons(self) -> None:
        """
        Create start and stop buttons to control timer.
        :return: None
        """
        self.start_button = Button(self.background, text="start", command=self.start_timer)
        self.background.create_window(10, 10, anchor="nw", window=self.start_button)

        self.stop_button = Button(self.background, text="stop", command=self.stop_timer)
        self.background.create_window(200, 10, anchor="nw", window=self.stop_button)

    def start_timer(self) -> None:
        """
        Start timer. Used as a callback in self.start_button.
        :return: None
        """
        self.timer_running = True
        self.timer()

    def stop_timer(self) -> None:
        """
        Stop timer. Used as a callback in self.stop_button.
        :return: None
        """
        self.timer_running = False

    def timer(self) -> None:
        """
        Display count down on widget, keep current time refreshed every second.
        :return: None
        """
        for current_time in time_utils.count_down(self.duration_sec):
            self.update_time(current_time)
            self.root.update()
            self.root.after(1000)
            if not self.timer_running:
                self.current_time = current_time
                break

    def update_time(self, current_time: str) -> None:
        """
        Update the self.timer_text widget with current time.
        :param current_time: str, current time in format "mm:ss"
        :return: None
        """
        self.background.itemconfig(self.timer_text, text=current_time)





