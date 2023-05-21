list_of_products = input().split()

for id, val in enumerate(list_of_products):
    print(f'{id + 1}. {val}')

