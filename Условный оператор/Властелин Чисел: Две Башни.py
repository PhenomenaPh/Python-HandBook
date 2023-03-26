x = sorted(str(input()))
if x[0] != '0':
    print(int(x[0] + x[1]), int(x[2] + x[1]))
else:
    print(int(x[1] + x[0]), int(x[2] + x[1]))
