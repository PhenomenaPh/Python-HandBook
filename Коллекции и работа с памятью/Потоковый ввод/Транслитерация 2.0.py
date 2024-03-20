with open('cyrillic.txt', 'r', encoding='utf-8') as f:
    cyrillic = f.read()

words = {
    'А': 'A',
    'Б': 'B',
    'В': 'V',
    'Г': 'G',
    'Д': 'D',
    'Е': 'E',
    'Ё': 'E',
    'Ж': 'Zh',
    'З': 'Z',
    'И': 'I',
    'Й': 'I',
    'К': 'K',
    'Л': 'L',
    'М': 'M',
    'Н': 'N',
    'О': 'O',
    'П': 'P',
    'Р': 'R',
    'С': 'S',
    'Т': 'T',
    'У': 'U',
    'Ф': 'F',
    'Х': 'Kh',
    'Ц': 'Tc',
    'Ч': 'Ch',
    'Ш': 'Sh',
    'Щ': 'Shch',
    'Ы': 'Y',
    'Э': 'E',
    'Ю': 'Iu',
    'Я': 'Ia',
    'Ъ': '',
    'Ь': '',
}

for i in list(words.keys()):
    words[i.lower()] = words[i].lower()

with open('transliteration.txt', 'w', encoding='utf-8') as file_in:
    for i in cyrillic:
        file_in.write(words.get(i, i))
