from itertools import product
statement = input()

possible_values = list(product([0, 1], repeat=3))

print('a b c f')
for i in possible_values:
    a, b, c = i
    print(f'{a} {b} {c} {int(eval(statement))}')