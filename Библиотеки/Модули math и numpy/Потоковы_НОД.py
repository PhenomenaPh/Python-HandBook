import math
from sys import stdin


gcd = 0

for line in stdin:
    numbs = list(map(int, line.split()))
    gcd = numbs[0]

    for i in range(len(numbs) - 1):
        gcd = math.gcd(gcd, numbs[i + 1])

    print(gcd)
