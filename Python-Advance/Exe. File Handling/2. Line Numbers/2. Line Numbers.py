marks = {",", '.', '?', "'", '-', '!', ':', ';', '_', '"'}

with open('text.txt', 'r') as file, open('output.txt', 'w') as output:
    index = 1
    for line in file:
        letters_counter = 0
        marks_counter = 0
        for ch in line:
            if ch in marks:
                marks_counter += 1
            elif ch.isalpha():
                letters_counter += 1
        output.write(f'Line {index}: {line.strip()} ({letters_counter})({marks_counter})')
        output.write('\n')
        index += 1