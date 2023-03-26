x = int(input())
start = 1
end = 2
flag = False

for i in range(x):
    for i in range(start, end):
        print(i, end =' ')
        
        if i == x:
            flag = True
            break
        
    if flag:
        break
    
    z = end - start
    
    start += z
    end += (z + 1)
    print('')