x = int(input())
y = int(input())

integer = x * y

while x != 0 and y != 0:
    if x > y:
        x = x % y
    else:
        y = y % x

print(integer // (x + y))
