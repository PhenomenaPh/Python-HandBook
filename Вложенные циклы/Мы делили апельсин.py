x = int(input())

print('А Б В')

for i in range(1, x + 1):
    for j in range(1, x + 1):
        for k in range(1, x + 1):
            if i + j + k == x:
                print(f'{i} {j} {k}')

