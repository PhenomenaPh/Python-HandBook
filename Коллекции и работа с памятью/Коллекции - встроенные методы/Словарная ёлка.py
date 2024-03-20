from itertools import accumulate

words = [[word] for word in input().split()]

for value in accumulate(words):
    print(' '.join(inner_value for inner_value in value))




