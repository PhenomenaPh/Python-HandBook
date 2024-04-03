import string
import pandas as pd


def clean_text_input(text: str) -> list:
    character_strip_table = text.maketrans("", "", string.punctuation + string.digits)
    return text.translate(character_strip_table).lower().split()


def length_stats(text: str):
    odd_words_dict = {}
    even_words_dict = {}

    clean_text = clean_text_input(text)

    for word in sorted(clean_text):
        if word in even_words_dict or word in odd_words_dict:
            continue
        word_length = len(word)
        if word_length % 2 == 0:
            even_words_dict[word] = word_length
        else:
            odd_words_dict[word] = word_length

    return pd.Series(odd_words_dict, dtype="int64"), pd.Series(
        even_words_dict, dtype="int64"
    )


odd, even = length_stats("Мама мыла раму")
print(odd)
print(even)
