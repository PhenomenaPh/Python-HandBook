x = input()
count = 0

for i in range(len(x)):
    count += 1

    if i == len(x) - 1:
        print(x[i], count)

    elif x[i] != x[i+1]:
        print(x[i], count)
        count = 0
    else:
        continue


