import sys

K, N = map(int, sys.stdin.readline().split())
listA = []
for i in range(K):
    listA.append(int(sys.stdin.readline()))
start = 1
end = max(listA)
while start <= end :
    mid = (start + end) // 2
    lines = 0
    for i in listA :
        lines += i // mid
    if lines >= N :
        start = mid + 1
    else :
        end = mid - 1
print(end)