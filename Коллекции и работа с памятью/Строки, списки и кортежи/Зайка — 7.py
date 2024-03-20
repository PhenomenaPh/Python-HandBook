x = int(input())

for i in range(x):
    word = input()
    ind = word.find('зайка')
    if ind == -1:
        print('Заек нет =(')
    else:
        print(ind + 1)