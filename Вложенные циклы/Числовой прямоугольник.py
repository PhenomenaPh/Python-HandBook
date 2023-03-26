x = int(input())
y = int(input())

start = 1
stop = y + start

for i in range(x):
    if x * y < 10:
        for j in range(start, stop):
            print(f'{j}', end=' ')
    else:
        for j in range(start, stop):
            length = len(str(x * y))
            print(f'{j:>{length}}', end=' ')
    
    start += y
    stop += y
    print('')
    
    