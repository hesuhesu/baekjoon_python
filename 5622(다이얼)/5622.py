import sys 

alpabetList = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
stringA = sys.stdin.readline()

result = 0
for i in stringA :
    for j in alpabetList :
        if i in j :
            result += alpabetList.index(j) + 3

print(result)
