x = int(input())
num = ''

for i in range(x):
    y = input()
    
    best_num = 0
    for j in y:
        if int(j) >= best_num:
            best_num = int(j)
    num += str(best_num)

print(num)
    
