x = str(input())
y = str(input())
z = str(input())

u = 'зайка'

print(x, y ,z)
if u in x:
    if u in y:
        if u in z:
            print(min(x, y, z), len(min(x, y, z)))
        else:
            print(min(x, y), len(min(x, y)))
    else:
        print(x, len(x))
        
elif u in y:
    if u in z:
        print(min(y, z), len(min(y, z)))
    else:
        print(y, len(y))
        
elif u in z:
    if u in x:
        print(min(x, z), len(min(x, z)))
    else:
        print(z, len(y))
    

