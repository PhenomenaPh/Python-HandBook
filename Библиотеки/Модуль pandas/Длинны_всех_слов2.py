import pandas as pd
import string


def length_stats(text: str):
    words_dict = dict()

    refactor_table = text.maketrans("", "", string.punctuation + string.digits)
    refactored_text = text.translate(refactor_table).lower().split()

    for word in sorted(refactored_text):
        if not words_dict.get(word, None):
            words_dict[word] = len(word)

    return pd.Series(words_dict)
