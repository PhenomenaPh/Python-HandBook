meal_num = int(input())
meal_dict = {}

for i in range(meal_num):
    meal = input()
    meal_dict[meal] = 0

days_num = int(input())

for i in range(days_num):
    num_of_meals = int(input())
    for j in range(num_of_meals):
        meal = input()
        meal_dict[meal] += 1

no_meal = True
for key, value in sorted(meal_dict.items()):
    if value == 0:
        print(key)
        no_meal = False

if no_meal:
    print('Готовить нечего')
