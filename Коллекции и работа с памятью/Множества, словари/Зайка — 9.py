
words_dict = {}
while (x := input()) != '':
    for i in x.split():
        words_dict[i] = words_dict.get(i, 0) + 1

for key, val in words_dict.items():
    print(key, val, end='\n')