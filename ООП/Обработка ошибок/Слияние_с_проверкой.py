def check_iter(iter1, iter2):
    if not hasattr(iter1, "__iter__") or not hasattr(iter2, "__iter__"):
        raise StopIteration
    return None


def check_inconsistent(iter1, iter2):
    iter1_cond = all(isinstance(i, type(iter1[0])) for i in iter1)
    iter2_cond = all(isinstance(i, type(iter2[0])) for i in iter2)

    if not iter1_cond or not iter2_cond:
        raise TypeError

    if not isinstance(iter1[0], type(iter2[0])):
        raise TypeError

    return None


def is_sorted(iter1, iter2):

    sort_check_1 = all([iter1[i] <= iter1[i + 1] for i in range(len(iter1) - 1)])
    sort_check_2 = all([iter2[i] <= iter2[i + 1] for i in range(len(iter2) - 1)])

    if not (sort_check_1 and sort_check_2):
        raise ValueError


def merge(sorted_list_1, sorted_list_2):
    check_iter(sorted_list_1, sorted_list_2)
    check_inconsistent(sorted_list_1, sorted_list_2)
    is_sorted(sorted_list_1, sorted_list_2)

    return sorted(list(sorted_list_1) + list(sorted_list_2))


# print(*merge(35, (1, 2, 3)))
# print(*merge([3, 2, 1], range(10)))
# print(*merge([1, "2", 3], range(10)))
# a = b = ("1", "2", "3")
# b = (1, 2, 3)
# print(*merge(a, b))
# print(*merge([1, 2, 3], "123456789"))
