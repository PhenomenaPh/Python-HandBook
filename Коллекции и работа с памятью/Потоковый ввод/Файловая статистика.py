name = input()

numbers = []
with open(name, 'r') as f:
    for i in f:
        numbers.extend(list(map(int, i.split())))

positive_numbers = sum(1 for i in numbers if i > 0)
print(len(numbers), positive_numbers, min(numbers), max(numbers), sum(numbers),
      round(sum(numbers) / len(numbers), 2), sep='\n')
