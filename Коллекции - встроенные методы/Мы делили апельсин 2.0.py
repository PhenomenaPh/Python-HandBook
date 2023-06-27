from itertools import product
num = int(input())

values = list(product(range(1, num + 1), repeat=2))

print('А Б В')
for value in values:
    value_sum = sum(value)
    if value_sum < num:
        print(f'{value[0]} {value[1]} {num - value_sum}')

