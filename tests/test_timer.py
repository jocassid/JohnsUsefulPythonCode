
from datetime import datetime, timedelta
from time import sleep

from timer import Timer


class TestTimer:

    @staticmethod
    def times_close_enough(expected, actual):
        return abs((expected - actual).total_seconds()) < 0.01

    def test_timer(self):

        sleep_seconds = 0.5
        timer = Timer()

        assert timer.total_seconds() is None

        expected_start_time = datetime.now()
        with timer:
            sleep(sleep_seconds)
        expected_end_time = datetime.now()

        assert self.times_close_enough(
            expected_start_time,
            timer.start_time,
        )

        assert self.times_close_enough(
            expected_end_time,
            timer.end_time,
        )

        elapsed = timer.elapsed
        assert isinstance(elapsed, timedelta)

        expected_elapsed = timedelta(seconds=sleep_seconds)
        diff = abs((expected_elapsed - elapsed).total_seconds())
        assert diff < 0.01

        assert timer.elapsed.total_seconds() == timer.total_seconds()
