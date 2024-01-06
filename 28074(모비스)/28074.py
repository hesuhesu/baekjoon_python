import sys

stringA = sys.stdin.readline().strip()
setA = set(stringA)
listA = ['M', 'O', 'B', 'I', 'S']
check = 0

for i in listA :
    if i not in setA :
        check += 1
        break
if check == 0 :
    print("YES")
else :
    print("NO")
