list_of_values = []


def enter_results(*args):
    for i in args:
        list_of_values.append(i)


def get_sum() -> tuple:
    even_sum = round(
        sum([val for idx, val in enumerate(list_of_values) if idx % 2 == 0]), 2
    )
    odd_sum = round(
        sum([val for idx, val in enumerate(list_of_values) if idx % 2 != 0]), 2
    )

    return even_sum, odd_sum


def get_average() -> tuple:
    even_nums = [val for idx, val in enumerate(list_of_values) if idx % 2 == 0]
    odd_nums = [val for idx, val in enumerate(list_of_values) if idx % 2 != 0]

    even_average = round(sum(even_nums) / len(even_nums), 2)
    odd_average = round(sum(odd_nums) / len(odd_nums), 2)

    return even_average, odd_average
