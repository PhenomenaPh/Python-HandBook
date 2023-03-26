len_str = int(input())
num_of_str = int(input())

for i in range(num_of_str):
    string = input()

    if len(string) > len_str:
        print(f'{string[:len_str - 3]}...')
    else:
        print(string)
