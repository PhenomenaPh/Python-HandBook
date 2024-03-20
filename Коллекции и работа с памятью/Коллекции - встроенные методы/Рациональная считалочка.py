from itertools import count

nums = input().split()

for value in count(float(nums[0]), float(nums[2])):
    if value <= float(nums[1]):
        print(round(value, 2))
    else:
        break