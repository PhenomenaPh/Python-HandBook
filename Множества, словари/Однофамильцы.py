num = int(input())
last_name_dict = {}

for i in range(num):
    last_name = input()

    last_name_dict[last_name] = last_name_dict.get(last_name, 0) + 1

list_of_non_unique_names = [count for count in last_name_dict.values() if count > 1]

print(sum(list_of_non_unique_names))