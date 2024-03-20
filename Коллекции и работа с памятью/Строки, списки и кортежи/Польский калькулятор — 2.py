x = input().split()
stack = list()

for i in range(len(x)):
    if x[i] == '+':
        a = stack[-2] + stack[-1]
        stack = stack[:-2]
        stack.append(a)
    elif x[i] == '-':
        a = stack[-2] - stack[-1]
        stack = stack[:-2]
        stack.append(a)
    elif x[i] == '*':
        a = stack[-2] * stack[-1]
        stack = stack[:-2]
        stack.append(a)
    elif x[i] == '/':
        a = stack[-2] // stack[-1]
        stack = stack[:-2]
        stack.append(a)
    elif x[i] == '*':
        a = stack[-2] * stack[-1]
        stack = stack[:-2]
        stack.append(a)
    elif x[i] == '~':
        stack[-1] = -stack[-1]
    elif x[i] == '!':
        num = 1
        for i in range(1, stack[-1] + 1):
            num *= i
        stack[-1] = num
    elif x[i] == '#':
        stack.append(stack[-1])
    elif x[i] == '@':
        stack[-3], stack[-2], stack[-1] = stack[-2], stack[-1], stack[-3]
    else:
        stack.append(int(x[i]))

print(stack[0])