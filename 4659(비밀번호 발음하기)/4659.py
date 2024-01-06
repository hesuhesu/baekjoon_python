import sys

listA = ['a','e','i','o','u']
accept = ['ee','oo']
while 1 :
    x=y=0
    stringA = sys.stdin.readline().strip()
    if stringA == 'end' :
        break
    
    count = 0 
    for i in listA :
        if i in stringA :
            count +=1 
     
    if count == 0 :
        print(f'<{stringA}> is not acceptable.')
        continue
    
    for i in range(len(stringA)-2) :
        if stringA[i] in listA and stringA[i+1] in listA and stringA[i+2] in listA :
            x = 1 
        elif not(stringA[i] in listA) and not(stringA[i+1]in listA) and not(stringA[i+2] in listA) :
            x = 1 
    if x == 1 :
        print(f'<{stringA}> is not acceptable.')
        continue

    for i in range(len(stringA)-1) :
        if stringA[i]==stringA[i+1] :
            if stringA[i] == 'e' or stringA[i] == 'o' :
                continue
            else :
                y = 1 
    if y == 1 :
        print(f'<{stringA}> is not acceptable.')
        continue

    print(f'<{stringA}> is acceptable.')
