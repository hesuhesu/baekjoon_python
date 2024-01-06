num, num_p = map(int, input().split())

listA = list(map(int, input().split()))
listA.sort()
print(listA[-num_p])
