x = input()
num_of_palim = 0

for i in range(int(x)):
    num = input()

    val = 0
    for j in range(len(num) // 2):
        if num[j] != num[len(num) - j - 1]:
            val += 1
                     
    if val == 0:
        num_of_palim += 1

print(num_of_palim)