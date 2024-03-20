num = int(input())

letters = [input().strip() for i in range(num)]
find_word = input().strip().lower()

for letter in letters:
    if letter.lower().find(find_word) != -1:
        print(letter)
