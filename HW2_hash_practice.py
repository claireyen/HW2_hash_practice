file_name = 'hw2_data.txt'
words = {}


def count_words():
    file = open(file_name, 'r')

    for line in file.readlines():
        line = line.replace('\n', '')
        if line in words:
            words[line] += 1
        else:
            words[line] = 1
        

count_words()
print(words)
