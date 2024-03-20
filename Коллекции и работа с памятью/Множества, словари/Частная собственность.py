num_children = int(input())
toys_dict = {}

for i in range(num_children):
    name, toys = input().split(': ', 1)

    for toy in set(toys.split(', ')):
        toys_dict[toy.strip()] = toys_dict.get(toy, 0) + 1

print(toys_dict)