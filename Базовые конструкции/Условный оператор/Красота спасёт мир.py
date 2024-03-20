x = int(input())

x1 = float(str(x)[0])
x2 = float(str(x)[1])
x3 = float(str(x)[2])

values = (x1, x2, x3)

max_val = int(max(values))
min_val = int(min(values))

if ((max_val + min_val) / 2) in values:
    print('YES')
else:
    print('NO')
