import math

n, m = list(map(int, input().split()))

all_comb = math.comb(n, m)
valid_cases = all_comb - math.comb(n - 1, m)

print(valid_cases, all_comb)
