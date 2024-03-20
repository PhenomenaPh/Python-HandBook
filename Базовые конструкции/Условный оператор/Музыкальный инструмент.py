x = int(input())
y = int(input())
z = int(input())

if x < (y + z):
    if y < (x + z):
        if z < (x + y):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('NO')