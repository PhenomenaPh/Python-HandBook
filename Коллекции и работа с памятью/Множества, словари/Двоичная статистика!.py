nums = input().split()
list_of_dicts = []

for i in nums:
    num = int(i)
    digit_dict = {'zeros': 0, 'units': 0, 'digits': 0}

    while num > 0:

        if num % 2 == 0:
            digit_dict['zeros'] += 1
        else:
            digit_dict['units'] += 1
        num //= 2

    digit_dict['digits'] = digit_dict['zeros'] + digit_dict['units']
    list_of_dicts.append(digit_dict)

print(list_of_dicts)