x = int(input())
y = int(input())

x = {input() for i in range(x)}
y = {input() for i in range(y)}

union_of_kids = x & y

if len(union_of_kids) == 0:
    print('Таких нет')
else:
    print(len(union_of_kids))