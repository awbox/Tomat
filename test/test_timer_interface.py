import unittest

from TabObject import TimerInterface


class TimerTest(unittest.TestCase):
    def setUp(self):
        self.subject = TimerInterface()

    def test_start_timer(self):
        self.subject.start_timer()
        assert self.subject.timer_running == True

    def test_stop_timer(self):
        self.subject.stop_timer()
        assert self.subject.timer_running == False
