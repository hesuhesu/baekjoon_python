import sys,math

stringA = list(map(str, sys.stdin.readline().strip()))
check = stringA[0]
count = 0
for i in range(1,len(stringA)) :
    if check != stringA[i] :
        check = stringA[i]
        count += 1

print(math.ceil(count/2))
