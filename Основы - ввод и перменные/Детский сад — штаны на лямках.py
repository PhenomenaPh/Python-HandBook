x = input()
y = int(input())

group_int = y // 100
kid_id = y % 10
bed = (y // 10) % 10

print(f'Группа №{group_int}.', f'{kid_id}. {x}.', f'Шкафчик: {y}.', f'Кроватка: {bed}.', sep='\n')