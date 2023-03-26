n = int(input('Enter the number:'))
k = 2 * n - 2
for i in range(0, n):
    for j in range(0, k):
        print(end= ' ')
    k = k - 1
    for j in range(0, i + 1):
        print(f'{i} ', end= '') # No space 
    print('') # No space
    
k = n - 2
for i in range(n, -1, -1):
    for j in range(k, 0, -1):
        print(end= ' ')
    k = k + 1
    for j in range(0, i + 1):
        print(f'{i} ', end= '') # No space
    print('') # No space