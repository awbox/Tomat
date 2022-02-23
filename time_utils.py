def time_in_seconds(mins: int, secs: int = 0) -> int:
    """
    Converts time to seconds.
    :param mins: int, minutes
    :param secs: int, seconds (default 0)
    :return: int, total time in seconds
    """
    return mins * 60 + secs


def time_display_format(time_seconds: int) -> str:
    """
    display time in formatted string.
    :param time_seconds: time in seconds
    :return: string, time in format "mm:ss"
    """
    return f"{time_seconds//60:02d}:{time_seconds%60:02d}"


def count_down(time_seconds: int):
    """
    Generator count down, yielding time string every second.
    :param time_seconds: time in seconds, start of count down
    :yield: string, formatted time "mm:ss" every second
    """
    while time_seconds > 0:
        yield time_display_format(time_seconds)
        time_seconds -= 1
