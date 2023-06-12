from itertools import islice, cycle

num = int(input())
dishes = [input() for i in range(num)]
iter = int(input())

for i in islice(cycle(dishes), iter):
    print(i)