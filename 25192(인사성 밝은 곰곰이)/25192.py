import sys

N = int(sys.stdin.readline())
count = 0
setA = set()
for i in range(N):
    stringA = sys.stdin.readline().strip()
    if (stringA == "ENTER"):
        count += len(setA)
        setA.clear()
        continue
    setA.add(stringA)
count += len(setA)
print(count)
