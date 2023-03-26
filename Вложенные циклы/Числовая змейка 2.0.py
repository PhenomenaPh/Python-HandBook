n = int(input())
m = int(input())
max_value = len(str(n * m))

if n > 0 and m > 0:
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (j % 2) != 0:
                num = j * n - n + i
            else:
                num = j * n + 1 - i
            print(f'{num:>{max_value}}', end=' ')      
        print('')