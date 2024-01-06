from collections import deque

while 1 :

    sentance = input()
    listA = list(sentance)
    dq = deque()
    
    if (len(listA) == 1) & (listA[0] == '.'):
        break

    result = 0
    for i in listA :
        if (i == '(') | (i == '['):
            dq.append(i)
        elif (i == ')') :
            if (len(dq) == 0)  :
                result += 1
                break
            elif (len(dq) > 0) & (dq[-1] == '[') :
                result += 1
                break
            else :
                dq.pop()
        elif (i == ']') :
            if (len(dq) == 0) :
                result += 1
                break
            elif (len(dq) > 0) & (dq[-1] == '(') :
                result += 1
                break
            else :
                dq.pop()

    
    if (result == 0) & (len(dq) == 0) :
        print('yes')
    else :
        print('no')
