count = int(input())
listA = list(map(int, input().split()))
sum = 0
for i in listA :
    sum += i

result = sum / len(listA)
listA.sort()
print(result / listA[-1] * 100)
