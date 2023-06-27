from itertools import chain
num = int(input())

values = list(chain(*[input().split(', ') for i in range(num)]))

for id, val in enumerate(sorted(values)):
    print(f'{id + 1}. {val}')