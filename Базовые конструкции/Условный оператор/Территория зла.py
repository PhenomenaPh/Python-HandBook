x = int(input())
y = int(input())
z = int(input())

if x >= y and x >= z:
    if x**2 > (y**2 + z**2):
        print('велика')
    elif x**2 == (y**2 + z**2):
        print('100%')
    else:
        print('крайне мала')
elif y >= x and y >= z:
    if y**2 > (x**2 + z**2):
        print('велика')
    elif y**2 == (x**2 + z**2):
        print('100%')
    else:
        print('крайне мала')
elif z >= x and z >= y:
    if z**2 > (x**2 + y**2):
        print('велика')
    elif z**2 == (x**2 + y**2):
        print('100%')
    else:
        print('крайне мала')
    