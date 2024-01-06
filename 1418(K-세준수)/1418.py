import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

listA = [0 for i in range(N+1)]
for i in range(2, N+1):
    if listA[i] == 0:
        for t in range(i, N+1, i):
            if t % i == 0:
                listA[t] = max(listA[t], i)
result = 0
for i in listA :
    if i <= M :
        result += 1
print(result-1)
