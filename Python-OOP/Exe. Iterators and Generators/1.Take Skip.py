class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.start = 0
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.count:
            raise StopIteration
        else:
            temp = self.number
            self.number += self.step
            self.start += 1
            return temp


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
