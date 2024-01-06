import sys

listA = list(map(int , sys.stdin.readline().split()))
index = 0
result = listA[0]
if (sum(listA) >= 100):
    print("OK")
else :
    for i in range(len(listA)) :
        if listA[i] < result :
            index = i
            result = listA[i]
    
    if index == 0 :
        print("Soongsil")
    elif index == 1 :
        print("Korea")
    else :
        print("Hanyang")
