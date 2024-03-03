import sys

T = int(sys.stdin.readline())
for i in range(T):
    strA = sys.stdin.readline().strip()
    result = ''
    count = 0
    index = 0
    for j in range(len(strA)) :
        if strA[j] == '0' or strA[j] == '1' :
            result = strA[j]
            index = j
            break
        count += 1
    
    if count % 2 == 0 :
        if index == len(strA) - 1:
            print(result)
        else :
            print(1)
    else :
        if index < len(strA) - 1 :
            print(0)
        elif index == len(strA) - 1 :
            if result == '0' :
                print(1)
            else :
                print(0)