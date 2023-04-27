x = int(input())

kids_dict = {}

for i in range(x):
    kid = input().split()

    if kid[0] not in kids_dict:
        kids_dict[kid[0]] = []
    kids_dict[kid[0]].extend(kid[1:])

meal = input()
kids_with_meal = []
for key, val in kids_dict.items():
    if meal in val:
        kids_with_meal.append(key)

if len(kids_with_meal) == 0:
    print('Таких нет')
else:
    print('\n'.join(sorted(kids_with_meal)))