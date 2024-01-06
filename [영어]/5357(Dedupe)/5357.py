import sys

N = int(sys.stdin.readline())

result = []
for i in range(N):
    stringA = sys.stdin.readline().strip()
    listA = []
    listA.append(stringA[0])
    for j in stringA : 
        if j != listA[-1] :
            listA.append(j)
    result.append(''.join(listA))

for i in result :
    print(i)
