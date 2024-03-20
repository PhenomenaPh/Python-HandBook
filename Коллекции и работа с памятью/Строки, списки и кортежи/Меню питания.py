menu = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']
x = int(input())
len_menu = len(menu)

for i in range(x):
    index = i % len_menu
    print(menu[index])


