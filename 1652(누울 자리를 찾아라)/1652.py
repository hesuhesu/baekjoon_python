import sys

n = int(sys.stdin.readline())
listA = []
r, c = 0, 0
cnt = 0
for i in range(n):
    listA.append(list(sys.stdin.readline().strip()))
for i in range(n):
    cnt = 0
    for j in range(n):
        if listA[i][j] == '.':
            cnt += 1
        else:
            cnt = 0
        if cnt == 2:
            r += 1
for i in range(n):
    cnt = 0
    for j in range(n):
        if listA[j][i] == '.':
            cnt += 1
        else:
            cnt = 0
        if cnt == 2:
            c += 1
print(r, c)
