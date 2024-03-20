x = ''.join(input().lower().split())
print(x)
if x[::-1] == x:
    print('YES')
else:
    print('NO')
