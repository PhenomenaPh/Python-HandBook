x = int(input())

name = None
value = 0

for i in range(x):
    new_name = input()
    new_value = 0
    for j in input():
        new_value += int(j)
        
    if new_value > value:
        name = new_name
        value = new_value
print(name)