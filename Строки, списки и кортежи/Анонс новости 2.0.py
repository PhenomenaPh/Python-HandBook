len_of_article = int(input())
num_sentences = int(input())

sentence = []

for i in range(num_sentences):
    sentence.append(input())

for i in sentence:
    length = len(i)
    diff = len_of_article - length
    if diff > 3:
        len_of_article -= length
        print(i)
    else:
        print(i[:len_of_article - 3] + '...')
        break