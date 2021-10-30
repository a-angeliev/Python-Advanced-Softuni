class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number -1
        self.new_seq = self.sequence
        self.index = 0
        while self.number > len(self.new_seq):
            self.new_seq += self.sequence

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > self.number:
            raise StopIteration
        else:
            temp = self.new_seq[self.index]
            self.index +=1
            return temp

result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')
