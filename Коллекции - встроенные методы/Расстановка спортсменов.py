from itertools import permutations
num = int(input())

names = sorted([input() for i in range(num)])

permutations_list = list(permutations(names, 3))

for value in permutations_list:
    print(', '.join(value))


