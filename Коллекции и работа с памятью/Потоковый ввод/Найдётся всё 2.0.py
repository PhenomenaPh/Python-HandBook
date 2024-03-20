from sys import stdin

lines = [line.rstrip('\n') for line in stdin.readlines()]

keywoard = lines.pop()

for i in lines:
    if keywoard.lower() in i.lower():
        print(i)
