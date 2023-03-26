x = int(input())
y = int(input())
    
if x <= y:
    for i in range(x, y + 1):
        print(i, end=' ')
else:
    for i in range(x, y - 1, -1):
        print(i, end=' ')
        