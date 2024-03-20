x = map(int, input().split())
initial_num = next(x)

for current_num in x:
    while current_num != 0 and initial_num != 0:
        if current_num > initial_num:
            current_num %= initial_num
        else:
            initial_num %= current_num

    initial_num += current_num

print(initial_num)
