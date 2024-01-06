import sys

listA = ['a', 'e', 'i', 'o', 'u']
intA = int(sys.stdin.readline())
stringA = sys.stdin.readline().strip()
result = 0
for i in stringA :
    if i in listA :
        result += 1

print(result)
