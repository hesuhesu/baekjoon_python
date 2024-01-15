import sys

line = list(sys.stdin.readline())
line.pop()
stack = []
count = 0
for i in range(len(line)) :
    if line[i] == '(' :
        stack.append('(')
    else :
        if (line[i-1] == '('):
            stack.pop()
            count += len(stack)
        else :
            stack.pop()
            count += 1
print(count)
