def merge_sort(values: list) -> list:
    store_values = []

    if len(values) == 1:
        return values

    slice_point = len(values) // 2

    slice1 = merge_sort(values[:slice_point])
    slice2 = merge_sort(values[slice_point:])

    i, j = 0, 0

    while len(slice1) != i and len(slice2) != j:
        if slice1[i] > slice2[j]:
            store_values.append(slice2[j])
            j += 1
        else:
            store_values.append(slice1[i])
            i += 1

    while len(slice1) != i:
        store_values.append(slice1[i])
        i += 1
    while len(slice2) != j:
        store_values.append(slice2[j])
        j += 1

    return store_values
