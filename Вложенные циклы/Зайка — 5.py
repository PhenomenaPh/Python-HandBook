x = int(input())
sum_of_territories = 0

for i in range(x):
    while (road := input()) != 'ВСЁ':
        inner_zayac = 0
        if road == 'зайка' and inner_zayac < 1:
            sum_of_territories += 1
            inner_zayac += 1
            
print(sum_of_territories)