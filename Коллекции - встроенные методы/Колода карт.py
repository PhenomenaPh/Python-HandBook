from itertools import chain, product
suit = input()

names_of_cards = list(chain([i for i in range(2, 11)],
                            ['валет', "дама", "король", "туз"]))

card_suit = [i for i in ['пик', "треф", "бубен", "червей"] if i != suit]

values = list(product(names_of_cards, card_suit))

for i in values:
    print(i[0], i[1])