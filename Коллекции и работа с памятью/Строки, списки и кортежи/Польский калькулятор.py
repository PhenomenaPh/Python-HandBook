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
    else:
        stack.append(int(x[i]))

print(stack[0])