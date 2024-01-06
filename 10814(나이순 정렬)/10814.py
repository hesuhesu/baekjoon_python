import sys

n = int(sys.stdin.readline().strip())

listA = []
for i in range(n):
    age, name = map(str, sys.stdin.readline().strip().split())
    age = int(age)
    listA.append([age, name])

listA.sort(key = lambda x : x[0])	## (age, name)에서 age만 비교

for i in listA :
    print(i[0], i[1])
