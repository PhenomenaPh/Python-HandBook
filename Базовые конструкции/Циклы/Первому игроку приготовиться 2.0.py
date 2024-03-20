x = int(input())

best_name = 'СамоеБольшоеСлово'
for i in range(x):
    name = input()
    if name <= best_name:
        best_name = name
print(best_name)