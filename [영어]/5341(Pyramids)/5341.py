import sys

while 1 :

    test = int(sys.stdin.readline())
    if test == 0 :
        break
    
    result = 0
    for i in range(1,test+1) :
        result += i
    print(result)
