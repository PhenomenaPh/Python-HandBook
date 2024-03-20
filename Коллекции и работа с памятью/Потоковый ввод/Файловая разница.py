import fileinput

first_file, second_file = input(), input()

words_1 = {word for line in fileinput.input(first_file) for word in line.split()}
words_2 = {word for line in fileinput.input(second_file) for word in line.split()}

final_words = sorted(words_1.symmetric_difference(words_2))

output_file = input()
with open(output_file, 'w') as file:
    file.write('\n'.join(final_words))