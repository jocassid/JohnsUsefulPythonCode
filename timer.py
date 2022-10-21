
from datetime import datetime


class Timer:

    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.elapsed = None

    def __enter__(self):
        self.start_time = datetime.now()
        self.end_time = None
        self.elapsed = None

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"exc_type is ", exc_type)
        self.end_time = datetime.now()
        self.elapsed = self.end_time - self.start_time
        return False

    def total_seconds(self):
        if not self.elapsed:
            return None
        return self.elapsed.total_seconds()

