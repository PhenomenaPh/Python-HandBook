from itertools import product
input_string = input()

variables = sorted(set([value for value in input_string if value.isupper()]))

print(f"{' '.join(variables)} F")
possible_values = list(product([0, 1], repeat=len(variables)))
for i in possible_values:
    env = dict(zip(variables, i))
    print(f'{" ".join(str(value) for value in i)} {int(eval(input_string, {}, env))}')