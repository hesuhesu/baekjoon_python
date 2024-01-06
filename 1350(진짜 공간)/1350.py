import sys, math

N = int(sys.stdin.readline())

listA = list(map(int, sys.stdin.readline().split()))
cls = int(sys.stdin.readline())

result = 0
for i in listA :
    if i % cls == 0 :
        if i == 0 :
            continue
        else :
            result += cls*(i // cls)
    else :
        result += cls*(math.ceil(i/cls))

print(result)
