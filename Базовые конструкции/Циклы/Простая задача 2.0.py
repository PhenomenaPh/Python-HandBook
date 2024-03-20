x = int(input())

const = 2
while x > 1:
    
    if x % const == 0:
        if int(x) == int(const):
            print(const, end='')
            x = x / const
        else:
            print(const, end=' * ')
            x = x / const
    else:
        const += 1

