name = str(input())
price = int(input())
weight = int(input())
cash = int(input())
print('=' * 16, 'Чек', '=' * 16, sep='')
print('Товар:', name.rjust(35 - 7))
print('Цена:', f'{weight}кг * {price}руб/кг'.rjust(35 - 6))
print('Итого:', f'{weight * price}руб'.rjust(35 - 7))
print('Внесено:', f'{cash}руб'.rjust(35 - 9))
print('Сдача:', f'{cash - (weight * price)}руб'.rjust(35 - 7))
print('=' * 35)