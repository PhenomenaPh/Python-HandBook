x = int(input())
coordinates_dict = {}

for i in range(x):
    coordinate1, coordinate2 = input().split()
    key = (int(coordinate1) // 10, int(coordinate2) // 10)

    coordinates_dict[key] = coordinates_dict.get(key, 0) + 1

print(max(coordinates_dict.values()))

