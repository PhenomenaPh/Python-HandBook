x = input()

val = 0
for i in range(len(x) // 2):
    if x[i] != x[len(x) - i - 1]:
        val += 1
        
if val == 0:
    print('YES')
else:
    print('NO')