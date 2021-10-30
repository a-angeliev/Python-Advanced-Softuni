def solution():

    def integers():
        n = 1
        while True:
            yield n
            n +=1

    def halves():

        for i in integers():
            yield i/2

    def take(n, seq):
        list = []
        for i in range(n):
            list.append(next(seq))
        return list
    return (take, halves, integers)

take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
