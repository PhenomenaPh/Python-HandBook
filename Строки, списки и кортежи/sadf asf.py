list_of_words = []
max_value = 0
order = 12312313

while (x := input()) != 'ФИНИШ':
    words = x.replace(' ', '').lower()
    list_of_words += words

for i in list_of_words:
    value = list_of_words.count(i)

    if value > max_value:
        max_value = value
        order = ord(i)
    elif value == max_value and ord(i) < order:
        max_value = value
        order = ord(i)

print(chr(order))
