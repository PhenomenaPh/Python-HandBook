value_list = [value for i in range(int(input())) for value in input().split()]

for i in set(value_list):
    print(i)