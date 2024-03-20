from itertools import chain
values = list(chain(*[input().split(', ') for i in range(3)]))

for id, val in enumerate(sorted(values)):
    print(f'{id + 1}. {val}')