import sys

n = int(sys.stdin.readline())

listA = []
for i in range(n) :
    listA.append("=" * (int(sys.stdin.readline())))

for i in listA :
    print(i)
