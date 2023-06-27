from itertools import product, combinations

suits_dict = {'буби': 'бубен', 'пики': 'пик', 'трефы': 'треф', 'черви': 'червей'}

suits = sorted(['червей', "бубен", "треф", "пик"])
ranks = sorted(["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"])

mustbe = suits_dict[input()]
excluded = input()

ranks.remove(excluded)
combinations_list = [f'{rank} {suit}' for rank, suit in list(product(ranks, suits))]

ThreeCards = list(combinations(combinations_list, 3))
ThreeCardCombination = sorted([value for value in ThreeCards if any(mustbe in word for word in value)])
print(ThreeCardCombination)

for i in ThreeCardCombination[:10]:
    print(', '.join(i))
