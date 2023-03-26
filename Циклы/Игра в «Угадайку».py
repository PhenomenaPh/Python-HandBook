left = 0
right = 1001
current = (left + right) // 2
answer = None

while answer != 'Угадал!':
    print(current)
    answer = input()

    if answer == 'Больше':
        left = current
    elif answer == 'Меньше':
        right = current
    current = (left + right) // 2
    
        