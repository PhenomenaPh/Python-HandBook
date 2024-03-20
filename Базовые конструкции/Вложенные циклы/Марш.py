x = int(input())
start = 1
end = 3
for i in range(1, x + 1):
    for j in range(end, start - 1, -1):
        if j != start:
            print(f'До старта {j} секунд(ы)')
        else:
            print(f'До старта {j} секунд(ы)')
            print(f'Старт {i}!!!')
    end += 1