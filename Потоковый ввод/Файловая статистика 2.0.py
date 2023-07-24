import json

file_name, json_name = input(), input()

with open(file_name, 'r') as f1, open(json_name, 'w') as f2:
    info_dict = dict()
    numbers = [int(i) for i in f1.read().split()]

    info_dict['count'] = len(numbers)
    info_dict['positive_count'] = len([i for i in numbers if i > 0])
    info_dict['min'] = min(numbers)
    info_dict['max'] = max(numbers)
    info_dict['sum'] = sum(numbers)
    info_dict['average'] = round(sum(numbers) / len(numbers), 2)

    json.dump(info_dict, f2, indent=2)