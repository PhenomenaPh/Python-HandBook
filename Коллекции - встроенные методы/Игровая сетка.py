from itertools import combinations
num = int(input())
names = [input() for i in range(num)]

for i in list(combinations(names, 2)):
    print(f'{i[0]} - {i[1]}')