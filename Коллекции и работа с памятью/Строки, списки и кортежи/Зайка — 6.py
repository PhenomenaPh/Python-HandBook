x = int(input())
values = 0

for i in range(x):
    word = input()

    for j in word.split(' '):
        if j == 'зайка':
            values += 1

print(values)
