from sys import stdin
import json
inputs = [line.strip() for line in stdin]


def parse_json(json_file: str, sum_of_values=0, values=list()):
    with open(json_file, 'r', encoding='UTF-8') as f1:
        lines = json.load(f1)
        for i in lines:
            for num in i['tests']:
                values.append((num['pattern'], i['points'] / len(i['tests'])))

    for i in range(len(inputs)):
        if inputs[i] == values[i][0]:
            sum_of_values += values[i][1]

    print(int(sum_of_values))


parse_json('scoring.json')
