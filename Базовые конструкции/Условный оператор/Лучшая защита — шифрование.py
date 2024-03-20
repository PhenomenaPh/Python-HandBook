x = int(input())

sum_low = (x // 10) % 10 + x % 10
sum_max = (x // 10) % 10 + x // 100

if sum_low > sum_max:
    print(sum_low, sum_max, sep='')
else:
    print(sum_max, sum_low, sep='')

