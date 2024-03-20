a = float(input())
b = float(input())
c = float(input())

D = b**2 - 4 * a * c
if a == 0 and b == 0 and c == 0:
    print('Infinite solutions')
elif a == 0 and b == 0 and c != 0:
    print('No solution')
elif a == 0 and b != 0:
    print(-c / b)    
elif D == 0:
    print(-b / (2 * a))
elif D < 0:
    print('No solution')
else:
    x1 = round((-b + D**(1 / 2)) / (2 * a), 2)
    x2 = round((-b - D**(1 / 2)) / (2 * a), 2)
    print(min(x1, x2), max(x1, x2))