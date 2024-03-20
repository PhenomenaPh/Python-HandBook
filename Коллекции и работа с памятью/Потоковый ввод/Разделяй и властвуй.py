file_name1, file_name2 = input(), input()
file_name3, file_name4 = input(), input()

with open(file_name1, 'r') as f1, open(file_name2, 'w') as f2, \
     open(file_name3, 'w') as f3, open(file_name4, 'w') as f4:
    for line in f1:
        line_even = []
        line_odd = []
        line_equal = []
        for num in line.split():
            digits = [int(i) for i in str(num)]
            even_count = sum(1 for d in digits if d % 2 == 0)
            odd_count = len(digits) - even_count

            if even_count > odd_count:
                line_even.append(num)
            elif odd_count > even_count:
                line_odd.append(num)
            else:
                line_equal.append(num)

        f2.write(' '.join(line_even) + '\n')
        f3.write(' '.join(line_odd) + '\n')
        f4.write(' '.join(line_equal) + '\n')

