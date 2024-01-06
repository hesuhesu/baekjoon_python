listA = []

for i in range(5) :
    listA.append(int(input()))

listA.sort()

print(int(sum(listA)/5))
print(listA[2])
