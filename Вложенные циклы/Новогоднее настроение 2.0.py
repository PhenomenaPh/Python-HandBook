n = int(input())

sum = 0
k = 0
while sum <= n:
    k += 1
    sum += k
x = k - sum + n

str1 = ''
for i in range(n - x + 1, n + 1):
    str1 += str(i) + ' '

str2 = ''
for i in range((n - x + 1) - k + 1, n - x + 1):
    str2 += str(i) + ' '

if len(str2) > len(str1):
    str1 = str2

len_max = len(str1)

i = 1
sum = 1
while i < k + 1:
    str1 = ''
    for g in range(0, i):
        if g + sum > n:
            break
        str1 += str(g + sum) + ' '
    sum += i
    i += 1
    print(f'{str1 : ^{len_max}}')



