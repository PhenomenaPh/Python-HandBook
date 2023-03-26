x = int(input())
y = int(input())
z = int(input())

petya = 43872 / x
vasya = 43872 / y
tolya = 43872 / z

if tolya > petya < vasya:
    print('Петя')
elif petya > tolya < vasya:
    print('Толя')
else:
    print('Вася')