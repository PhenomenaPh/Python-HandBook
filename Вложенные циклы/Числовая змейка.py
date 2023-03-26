x = int(input())
y = int(input())

start = 1
stop = y + start
count = 1

for i in range(x):
    if x * y < 10:
        if count % 2 != 0:
            for j in range(start, stop):
                print(f'{j}', end=' ')
        else:
            for j in range(stop - 1, start - 1, -1):
                print(f'{j}', end=' ')
    else:
        if count % 2 != 0:
            for j in range(start, stop):
                length = len(str(x * y))
                print(f'{j:>{length}}', end=' ')
        else:
            for j in range(stop - 1, start - 1, -1):
                length = len(str(x * y))
                print(f'{j:>{length}}', end=' ')
    count += 1
    start += y
    stop += y
    
    print('')