import sys

while 1 :
    try :
        N = int(sys.stdin.readline())
    except :
        break
    i = 1
    num = 0
    
    while 1 :
        num = num * 10 + 1
        if num % N == 0 :
            print(i)
            break
        i += 1