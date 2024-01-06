import sys

A,B = map(str, sys.stdin.readline().strip().split())

result = []
for i in range(len(B) - len(A) + 1):
    check = 0
    for j in range(len(A)):
        if A[j] != B[i + j]:
            check += 1
    result.append(check)

print(min(result))
