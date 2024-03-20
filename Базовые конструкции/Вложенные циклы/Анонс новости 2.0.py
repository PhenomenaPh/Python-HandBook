length = int(input())
sentences = int(input())

page = ''

for i in range(sentences):
    page += input() + '\n'
symbols = page[:length - 3].count('\n')

if len(page.replace('\n', '')) <= 4:
    print(page[:length] + '...')
elif len(page) > length:
    print(page[:length + symbols - 3] + '...')
else:
    print(page)