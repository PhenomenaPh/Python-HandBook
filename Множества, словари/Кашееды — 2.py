x = int(input())
y = int(input())

set_1 = set()
set_2 = set()

for v in range(x + y):
    i = input()
    if i in set_1:
        set_2.add(i)
    else:
        set_1.add(i)

unique_values = sorted(set_1 ^ set_2)
if len(unique_values) == 0:
    print('Таких нет')
else:
    print('\n'.join(unique_values))