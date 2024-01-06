from itertools import combinations # 리스트에서 조합을 구해줌
 
## 맵크기(N), 치킨집 최대 선택가능개수(M)
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
 
## 빈칸(0), 집(1), 치킨집(2)
houseList = []
chickenList = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1: 
            houseList.append((i, j))
        elif board[i][j] == 2: 
            chickenList.append((i, j))
 
minnum = float('inf') # 무한대 표시. '-inf'는 마이너스 무한대
for ch in combinations(chickenList, M):
    sumnum = 0
    for home in houseList:
        sumnum += min([abs(home[0]-i[0])+abs(home[1]-i[1]) for i in ch])
        if minnum <= sumnum: 
            break
    if sumnum < minnum: 
        minnum = sumnum
print(minnum)
