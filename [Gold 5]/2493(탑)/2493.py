import sys

N = int(sys.stdin.readline())

tower = list(map(int, sys.stdin.readline().split()))
stack = []
result = [0] * N

for i in range(N) :
    while stack :
        if stack[-1][1] > tower[i] :
            result[i] = stack[-1][0] + 1
            break
        else :
            stack.pop()
    stack.append([i, tower[i]])

for i in result :
    print(i, end=' ')
