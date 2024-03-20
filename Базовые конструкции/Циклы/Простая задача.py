x = int(input())

delim = 2

while delim ** 2 <= x and x % delim != 0:
    delim += 1


if x == 1:
    print('NO')
elif delim ** 2 > x:
    print('YES')
else:
    print('NO')