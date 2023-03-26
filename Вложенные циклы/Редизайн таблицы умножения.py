x = int(input())
length = int(input())
punctuation = length * x + (x - 1)

for i in range(1, x + 1):
    for j in range(1, x + 1):
        if j != x:
            print(f'{i * j : ^{length}}|', end='')
        else:
            print(f'{i * j : ^{length}}', end='')
    
    print('')

    if i != x:
        print('-' * punctuation)