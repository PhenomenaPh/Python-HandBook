x = int(input())

sum_of_num = 0

for i in range(x):
    value = input()
    for _ in value:
        sum_of_num += int(_)

print(sum_of_num)