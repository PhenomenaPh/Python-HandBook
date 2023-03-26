while (x := input()) != '':
    word_without_space = x.lstrip()
    if word_without_space.find('#') == 0:
        continue
    elif x.find('#') == -1:
        print(x)
    else:
        ind = x.find('#')
        print(x[:ind])