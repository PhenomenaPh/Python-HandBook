from itertools import chain, permutations
num = int(input())

food = list(chain(*[input().split(', ') for i in range(num)]))

combinations = list(permutations(sorted(food), 3))

for i in combinations:
    print(*i)

