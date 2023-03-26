x = input()

max_val = 0

for i in x:
    if int(i) >= max_val:
        max_val = int(i)
print(max_val)