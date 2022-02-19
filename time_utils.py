def time_in_seconds(mins, secs=0):
    return mins * 60 + secs


def time_display_format(time_seconds):
    return f"{time_seconds//60:02d}:{time_seconds%60:02d}"


def count_down(time_seconds):
    while time_seconds > 0:
        yield time_display_format(time_seconds)
        time_seconds -= 1