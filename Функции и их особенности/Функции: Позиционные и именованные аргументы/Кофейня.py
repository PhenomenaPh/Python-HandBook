def order(*args):
    drinks = {
        "Эспрессо": {"coffee": 1},
        "Капучино": {"coffee": 1, "milk": 3},
        "Макиато": {"coffee": 2, "milk": 1},
        "Кофе по-венски": {"coffee": 1, "cream": 2},
        "Латте Макиато": {"coffee": 1, "milk": 2, "cream": 1},
        "Кон Панна": {"coffee": 1, "cream": 1},
    }

    for drink in args:
        ingredients = drinks.get(drink)

        if all(ingredients[i] <= in_stock[i] for i in ingredients.keys()):
            for i in in_stock.keys():
                in_stock[i] -= ingredients.get(i, 0)
            return drink

    return "К сожалению, не можем предложить Вам напиток"
