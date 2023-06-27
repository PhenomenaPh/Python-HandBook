from itertools import product
nums = int(input())

for id, val in enumerate(list(product(range(1, nums + 1), repeat=2))):
    if (id + 1) % nums == 0:
        print(val[0] * val[1])
    else:
        print(val[0] * val[1], end=' ')