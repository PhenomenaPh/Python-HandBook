import math

x = float(input())

part_1 = math.log(x ** (3 / 16), 32)
part_2 = x ** (math.cos(math.pi * x / (2 * math.e)))
part_3 = math.sin(x / math.pi) ** 2

answer = part_1 + part_2 - part_3
print(answer)
