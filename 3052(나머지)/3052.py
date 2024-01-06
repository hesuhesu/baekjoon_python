listA = []

for i in range(10) :
    test_num = int(input())
    listA.append(test_num % 42)

setA = set(listA)

print(len(setA))
