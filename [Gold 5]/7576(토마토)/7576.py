import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dq = deque([])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
result = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            dq.append([i, j])

def bfs():
    while dq :
        x, y = dq.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                dq.append([nx, ny])

bfs()
for i in matrix:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    result = max(result, max(i))
print(result - 1)
