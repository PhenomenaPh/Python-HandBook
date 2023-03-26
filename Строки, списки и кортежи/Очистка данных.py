while (x := input()) != '':
    if x[-3:] == '@@@':
        continue
    else:
        x = x.lstrip('##')
    print(x)