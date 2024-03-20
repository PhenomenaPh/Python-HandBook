def secret_replace(sentence: str, **kwargs) -> str:
    replaced_list = []
    replacement_dict = {key: 0 for key in kwargs}

    for value in sentence:
        if value not in kwargs:
            replaced_list.append(value)
        else:
            replaced_list += kwargs[value][replacement_dict[value]]
            replacement_dict[value] = (replacement_dict[value] + 1) % len(kwargs[value])
    return "".join(replaced_list)
