x = 0
y = 0
while (direct := input()) != 'СТОП':
    move = int(input())
    
    if direct == 'СЕВЕР':
        y += move
    elif direct == 'ЗАПАД':
        x -= move
    elif direct == 'ВОСТОК':
        x += move
    else:
        y -= move

print(y, x, sep='\n')