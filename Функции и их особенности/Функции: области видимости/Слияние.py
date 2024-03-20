def merge(sorted_list_1, sorted_list_2) -> tuple:

    if not hasattr(sorted_list_1, "__iter__") or not hasattr(sorted_list_2, "__iter__"):
        raise StopIteration
    if (
        len(set(type(item) for item in sorted_list_1)) > 1
        or len(set(type(item) for item in sorted_list_2)) > 1
    ):
        raise TypeError
    if not all(
        [
            sorted_list_1[i] <= sorted_list_1[i + 1]
            for i in range(len(sorted_list_1) - 1)
        ]
    ) or not all(
        [
            sorted_list_2[i] <= sorted_list_2[i + 1]
            for i in range(len(sorted_list_2) - 1)
        ]
    ):
        raise ValueError

    store_list = []

    while len(sorted_list_1) > 0 and len(sorted_list_2) > 0:

        if sorted_list_1[0] < sorted_list_2[0]:
            store_list.append(sorted_list_1[0])
            sorted_list_1 = sorted_list_1[1:]
        else:
            store_list.append(sorted_list_2[0])
            sorted_list_2 = sorted_list_2[1:]
    while len(sorted_list_1) > 0:
        store_list.append(sorted_list_1[0])
        sorted_list_1 = sorted_list_1[1:]
    while len(sorted_list_2) > 0:
        store_list.append(sorted_list_2[0])
        sorted_list_2 = sorted_list_2[1:]

    return tuple(store_list)
