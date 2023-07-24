import json
from sys import stdin

file_name = input()

with open(file_name, 'r', encoding='UTF-8') as file:
    records = json.load(file)

for row in stdin:
    line = row.strip().split(' == ')
    records[line[0]] = line[1]

with open(file_name, 'w', encoding='UTF-8') as file:
    json.dump(records, file, ensure_ascii=False, indent=2)
