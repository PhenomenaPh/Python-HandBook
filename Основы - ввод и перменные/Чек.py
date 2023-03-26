product = input()
price = int(input())
weight = int(input())
money = int(input())

Price_for_weight = price * weight
change = money - price * weight

print('Чек', f'{product} - {weight}кг - {price}руб/кг', f'Итого: {Price_for_weight}руб', 
      f'Внесено: {money}руб', f'Сдача: {change}руб', sep='\n')