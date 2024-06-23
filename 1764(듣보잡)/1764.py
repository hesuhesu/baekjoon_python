import sys

N, M = map(int, sys.stdin.readline().split())
setA = set()
setB = set()
for i in range(N):
    setA.add(sys.stdin.readline().strip())

for i in range(M):
    setB.add(sys.stdin.readline().strip())

result = sorted(list(setA & setB))
print(len(result))
for i in result :
    print(i)
