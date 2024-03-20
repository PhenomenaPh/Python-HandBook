products = set(input() for i in range(int(input())))
products_for_dish = {}

for i in range(int(input())):  # Для каждого блюда - ключ сохраняем необходимые продукты - значение
    dish = input()
    num_products_for_dish = int(input())

    for i in range(num_products_for_dish):
        product = input()
        products_for_dish[dish] = products_for_dish.get(dish, set()) | {product}

can_create_dish = False

for key, value in sorted(products_for_dish.items()):
    if value <= products:
        print(key)
        can_create_dish = True

if can_create_dish is False:
    print('Готовить нечего')