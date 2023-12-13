class DaysOfWeekIterator:
    def __init__(self, start_day):
        self.days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.start_index = self.days_of_week.index(start_day)  
        self.index = self.start_index

    def __iter__(self):
        return self

    def __next__(self):
        day = self.days_of_week[self.index]
        self.index = (self.index + 1) % len(self.days_of_week)  
        return day

start_day = "Wednesday"
days_of_week_iterator = DaysOfWeekIterator(start_day)

for _ in range(10):
    print(next(days_of_week_iterator))
