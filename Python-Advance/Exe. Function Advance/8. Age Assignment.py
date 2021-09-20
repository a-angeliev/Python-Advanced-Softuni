def age_assignment(*args, **kwargs):
    new_dict = {}
    for el in args:
        letter = el[:1]
        for key,value in kwargs.items():
            if key == letter:
                new_dict[el] = value

    return new_dict

print(age_assignment("Peter", "George", G=26, P=19))