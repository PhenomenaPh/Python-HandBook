input_number = int(input())
max_digit_sum = 0
optimal_base = 10

for base in range(2, 11):
    temp_number = input_number
    digit_sum = 0

    while temp_number != 0:
        digit_sum += temp_number % base
        temp_number //= base

    if digit_sum > max_digit_sum or (
        digit_sum == max_digit_sum and base < optimal_base
    ):
        max_digit_sum = digit_sum
        optimal_base = base

print(optimal_base)
