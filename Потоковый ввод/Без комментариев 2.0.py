from sys import stdin

lines = [line.rstrip() for line in stdin]  # rstrip удаляет пробелы справа

for i in lines:
    if i.lstrip().startswith('#'):  # lstrip удаляет пробелы слева
        continue
    elif i.find('#') == -1:
        print(i)
    else:
        ind = i.find('#')
        print(i[:ind])

