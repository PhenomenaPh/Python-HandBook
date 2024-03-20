x = int(input())
okay = 0
h = 0
for i in range(x):

    if i == 0:
        h1 = 0
    else:
        h1 = h

    b = int(input())
    h = b % 256
    b = b // 256
    r = b % 256
    b = b // 256
    m = b 

    hash = 37 * (m + r + h1) % 256

    if (h != hash or h >= 100) and okay == 0:
        print(i)
        okay = 1
    
if okay == 0:
    print(-1)