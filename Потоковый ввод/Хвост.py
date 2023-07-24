file_name, num_of_rows = input(), int(input())

with open(file_name, 'r', encoding='UTF8') as f1:
    lines = [line.strip() for line in f1]

for line in lines[-num_of_rows:]:
    print(line)
