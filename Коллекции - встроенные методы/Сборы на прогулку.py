first_kids = input().split(', ')
second_kids = input().split(', ')

for i in list(zip(first_kids, second_kids)):
    print(f'{i[0]} - {i[1]}')
