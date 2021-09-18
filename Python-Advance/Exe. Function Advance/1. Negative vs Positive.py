def pos_or_neg(*args):
    pos_sum = 0
    neg_sum = 0

    for el in args[0]:
        if el.isdigit():
            pos_sum += int(el)
        elif el.lstrip("-").isdigit():
            neg_sum += int(el)

    print(neg_sum)
    print(pos_sum)
    if -neg_sum > pos_sum:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")

pos_or_neg(input().split())