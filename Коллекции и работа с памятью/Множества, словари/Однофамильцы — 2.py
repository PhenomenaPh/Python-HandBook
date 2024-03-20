num = int(input())
names_dict = {}

for i in range(num):
    name = input()

    names_dict[name] = names_dict.get(name, 0) + 1

names_dict = sorted(names_dict.items())
num_of_uniq_names = False

for name, count in names_dict:

    if count > 1:
        print(f'{name} - {count}')
        num_of_uniq_names = True

if not num_of_uniq_names:
    print('Однофамильцев нет')