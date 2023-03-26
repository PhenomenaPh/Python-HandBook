Petya = int(input())
Vasya = int(input())
Tolya = int(input())

if Petya > Vasya and Petya > Tolya:
    if Vasya > Tolya:
        print(' ' * 10, 'Петя', ' ' * 10, sep='')
        print(' ' * 2, 'Вася', ' ' * 18, sep='')
        print(' ' * 18, 'Толя', ' ' * 3, sep='')
        print(' ' * 3, 'II', ' ' * 6, 'I', ' ' * 6, 'III', ' ' * 4, sep='')
    else:
        print(' ' * 10, 'Петя', ' ' * 10, sep='')
        print(' ' * 2, 'Толя', ' ' * 18, sep='')
        print(' ' * 18, 'Вася', ' ' * 3, sep='')
        print(' ' * 3, 'II', ' ' * 6, 'I', ' ' * 6, 'III', ' ' * 4, sep='')
if Vasya > Petya and Vasya > Tolya:
    if Petya > Tolya:
        print(' ' * 10, 'Вася', ' ' * 10, sep='')
        print(' ' * 2, 'Петя', ' ' * 18, sep='')
        print(' ' * 18, 'Толя', ' ' * 3, sep='')
        print(' ' * 3, 'II', ' ' * 6, 'I', ' ' * 6, 'III', ' ' * 4, sep='')
    else:
        print(' ' * 10, 'Вася', ' ' * 10, sep='')
        print(' ' * 2, 'Толя', ' ' * 18, sep='')
        print(' ' * 18, 'Петя', ' ' * 3, sep='')
        print(' ' * 3, 'II', ' ' * 6, 'I', ' ' * 6, 'III', ' ' * 4, sep='')
if Tolya > Petya and Tolya > Vasya:
    if Petya > Vasya:
        print(' ' * 10, 'Толя', ' ' * 10, sep='')
        print(' ' * 2, 'Петя', ' ' * 18, sep='')
        print(' ' * 18, 'Вася', ' ' * 3, sep='')
        print(' ' * 3, 'II', ' ' * 6, 'I', ' ' * 6, 'III', ' ' * 4, sep='')
    else:
        print(' ' * 10, 'Толя', ' ' * 10, sep='')
        print(' ' * 2, 'Вася', ' ' * 18, sep='')
        print(' ' * 18, 'Петя', ' ' * 3, sep='')
        print(' ' * 3, 'II', ' ' * 6, 'I', ' ' * 6, 'III', ' ' * 4, sep='')