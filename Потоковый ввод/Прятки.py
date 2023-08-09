with open('secret.txt', 'r', encoding="UTF-8") as f:
    lines = f.read().strip()


def get_right_symbol(sentence: str):
    for i in sentence:
        if ord(i) >= 128:
            last_byte = ord(i) & 0xFF
            print(chr(last_byte), end='')
        else:
            print(i, end='')


get_right_symbol(lines)
