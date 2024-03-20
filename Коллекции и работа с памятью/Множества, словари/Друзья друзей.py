first_names_dict = {}
second_names_dict = {}
while (x := input()) != '':
    words = x.split()

    for id, word in enumerate(words):
        if id == 0:
            first_names_dict[word] = first_names_dict.get(word, []) + [words[id + 1]]
        else:
            first_names_dict[word] = first_names_dict.get(word, []) + [words[id - 1]]

for person in list(first_names_dict.keys()):
    second_level_friends = []
    for friend in first_names_dict[person]:
        for potential_second_level_friend in first_names_dict[friend]:
            if potential_second_level_friend not in first_names_dict[person] and potential_second_level_friend != person:
                if potential_second_level_friend not in second_level_friends:
                    second_level_friends.append(potential_second_level_friend)
    second_names_dict[person] = second_level_friends

for i in sorted(second_names_dict.keys()):
    second_names_dict[i].sort()
    print(f'{i}: {", ".join(second_names_dict[i])}')

