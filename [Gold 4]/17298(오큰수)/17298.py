import sys

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
answer = [-1] * N

stack = []
stack.append(0)
for i in range(1, N):
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)

print(*answer)