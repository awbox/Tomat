from time_utils import count_down, time_display_format, time_in_seconds


def test_time_in_seconds_minutes_no_seconds():
    minutes = 10
    expected_result = 600

    assert time_in_seconds(minutes) == expected_result


def test_time_in_seconds_minutes_and_seconds():
    minutes = 10
    seconds = 9
    expected_result = 609

    assert time_in_seconds(minutes, seconds) == expected_result


def test_time_in_seconds_zero_minutes():
    minutes = 0
    expected_result = 0

    assert time_in_seconds(minutes) == expected_result


def test_time_display_format_single_digit():
    time_seconds = 61
    expected_output = "01:01"

    assert time_display_format(time_seconds) == expected_output


def test_time_display_format_double_digits():
    time_seconds = 650
    expected_output = "10:50"

    assert time_display_format(time_seconds) == expected_output


def test_count_down():
    time_seconds = 3
    expected_output = ["00:03", "00:02", "00:01"]

    result = [timer_display for timer_display in count_down(time_seconds)]

    assert result == expected_output
