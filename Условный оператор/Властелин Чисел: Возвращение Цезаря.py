x = input()
y = input()
all_num = sorted(x + y)

max_val = int(max(x + y))
min_val = int(min(x + y))

sum_val = (int(all_num[1]) + int(all_num[2])) % 10
print(max_val, sum_val, min_val, sep='')