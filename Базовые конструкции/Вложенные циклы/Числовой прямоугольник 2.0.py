x = int(input())
y = int(input())

step = x
min = ((x * y) - step) + 1

for i in range(1, x + 1):
    if x * y < 10:
        for j in range(i, min + 1, step):
            print(f'{j}', end=' ')
    else:
        for j in range(i, min + 1, step):
            length = len(str(x * y))
            print(f'{j:>{length}}', end=' ')
        
    min += 1

    print('')
