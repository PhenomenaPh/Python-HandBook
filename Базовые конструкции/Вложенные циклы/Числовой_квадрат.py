n = int(input())
if n % 2 == 0:
    length = len(str(n // 2))
else:
    length = len(str(n // 2 + 1))

for row in range(1, n + 1):
    for col in range(1, n + 1):
        symbol = min(row, col, n - row + 1, n - col + 1)

        if col == n:
            print(f"{symbol:>{length}}", end="\n")
        else:
            print(f"{symbol:>{length}}", end=" ")
