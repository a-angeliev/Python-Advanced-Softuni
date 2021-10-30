class dictionary_iter():
    def __init__(self, info):
        self.info = info
        self.end = len(info) - 1
        self.index = 0
        self.list_dict = list(self.info.items())

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > self.end:
            raise StopIteration
        else:
            temp = self.list_dict[self.index]
            self.index +=1
            return temp


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)


result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
