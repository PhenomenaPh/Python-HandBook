def get_key(d, value):
    for key, v in d.items():
        if v == value:
            return key


def caesar_cipher(letter, shift):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    words_dict = {word: index for index, word in enumerate(alphabet)}
    new_text = ''
    
    for i in letter:
        if i.upper() in words_dict:
            new_index = (words_dict[i.upper()] + shift) % len(alphabet)
            new_text += get_key(words_dict, new_index) if i.isupper() else get_key(words_dict, new_index).lower()
        else:
            new_text += i
            
    return new_text


shift_value = int(input())

with open('public.txt', 'r') as f1, open('private.txt', 'w') as f2:
    lines = f1.read().strip()
    f2.write(caesar_cipher(lines, shift_value))
    
