x = int(input())
y = int(input())


Number_1_x = x // 100
Number_2_x = (x // 10) % 10
Number_3_x = x % 10


Number_1_y = y // 100
Number_2_y = (y // 10) % 10
Number_3_y = y % 10

Number_1 = (Number_1_x + Number_1_y) % 10
Number_2 = (Number_2_x + Number_2_y) % 10
Number_3 = (Number_3_x + Number_3_y) % 10

print(f"{Number_1}{Number_2}{Number_3}")