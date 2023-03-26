x = int(input())
y = int(input())
z = int(input())

if y < x > z:
    print('1. Петя')
    if y > z:
        print('2. Вася')
        print('3. Толя')
    else:
        print('2. Толя')
        print('3. Вася')
    
elif x < y > z:
    print('1. Вася')
    
    if x > z:
        print('2. Петя')
        print('3. Толя')
    else:
        print('2. Толя')
        print('3. Петя')

elif x < z > y:
    print('1. Толя')
    
    if x > y:
        print('2. Петя')
        print('3. Вася')
    else:
        print('2. Вася')
        print('3. Петя')


    