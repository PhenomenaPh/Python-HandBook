from sys import stdin

total = 0
for line in stdin:
    total += sum(int(i) for i in line.split())

print(total)