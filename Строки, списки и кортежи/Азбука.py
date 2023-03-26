x = int(input())
word = 0

for i in range(x):
    _ = input()
    if _[0].lower() in ['а', 'б', 'в']:
        word += 1

if word == x:
    print('YES')
else:
    print('NO')
