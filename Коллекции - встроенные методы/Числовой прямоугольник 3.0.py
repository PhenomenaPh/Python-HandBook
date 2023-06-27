from itertools import product
rows = int(input())
columns = int(input())

combinations = list(product(range(rows), range(columns)))

counter = 1
for i, j in combinations:
    if j == 0 and i != 0:
        print()
    print(f'{counter:>{len(str(rows * columns))}}', end=' ')
    counter += 1
