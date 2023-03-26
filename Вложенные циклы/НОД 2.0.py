x = int(input())

y = int(input())

for i in range(x - 1):
    z = int(input())
    while y != 0 and z != 0:
        if y > z:
            y = y % z
        else:
            z = z % y
    y = y + z

print(y)
        