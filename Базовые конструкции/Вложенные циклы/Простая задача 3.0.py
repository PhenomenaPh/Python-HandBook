x = int(input())
num = 0
for i in range(x):
    y = int(input())
    
    delim = 2
    while delim ** 2 <= y and y % delim != 0:
        delim += 1

    if delim ** 2 > y and y != 1:
        num += 1

print(num)