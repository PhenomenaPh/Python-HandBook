seen_objects = set()

while (sentence := input()) != '':
    words = sentence.split()

    for id, val in enumerate(words):
        if val == 'зайка':
            if id > 0:  # Если это не первое слово в предложении, то берем прошлое слово
                seen_objects.add(words[id - 1])
            if id < len(words) - 1:  # Если это не последнее слово в предложении, то берем следующее слово
                seen_objects.add(words[id + 1])
for obj in seen_objects:
    print(obj)