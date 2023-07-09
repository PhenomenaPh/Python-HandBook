from sys import stdin

lines = [line.split() for line in stdin]

last_month = [int(line[1]) for line in lines]
actual = [int(line[2]) for line in lines]

average_before = sum(last_month) / len(last_month)
average_actual = sum(actual) / len(actual)

print(round(average_actual - average_before))