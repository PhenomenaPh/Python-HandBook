import math

values = list(map(float, input().split()))

avg_geom = math.pow(math.prod(values), 1 / len(values))

print(avg_geom)
