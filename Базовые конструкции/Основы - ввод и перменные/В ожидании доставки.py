H = int(input())
M = int(input())
T = int(input())


Minutes = (M + T) % 60
Hours = (H + (T + M) // 60) % 24

Hours_1 = Hours // 10
Hours_2 = Hours % 10

Minutes_1 = Minutes // 10
Minutes_2 = Minutes % 10 
print(f'{Hours_1}{Hours_2}:{Minutes_1}{Minutes_2}')