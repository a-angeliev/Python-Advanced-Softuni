class Time():
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        cur_hour = f'0{self.hours}' if self.hours < 10 else self.hours
        cur_min = f'0{self.minutes}' if self.minutes < 10 else self.minutes
        cur_sec = f'0{self.seconds}' if self.seconds < 10 else self.seconds
        return f"{cur_hour}:{cur_min}:{cur_sec}"

    def next_second(self):
        if not self.seconds == Time.max_seconds:
            self.seconds += 1
            return self.get_time()
        elif not self.minutes == Time.max_minutes:
            self.minutes += 1
            self.seconds = 0
            return self.get_time()
        elif not self.hours == Time.max_hours:
            self.hours += 1
            self.minutes = 0
            self.seconds = 0
            return self.get_time()
        else:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
            return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())
