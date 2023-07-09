from sys import stdin

lines = stdin.read().split()

words = sorted(set(word for word in lines if word.lower() == word.lower()[::-1]))

for i in words:
    print(i)
    