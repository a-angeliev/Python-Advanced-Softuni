def fibonacci():
    prev_num =0
    yield prev_num
    cur_num =1
    yield cur_num
    while True:
        reuslt = prev_num + cur_num
        yield reuslt
        prev_num, cur_num = cur_num, reuslt

generator = fibonacci()
for i in range(5):
    print(next(generator))

