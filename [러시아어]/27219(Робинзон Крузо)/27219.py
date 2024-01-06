import sys

n = int(sys.stdin.readline())
stringA = ''
if n//5 == 0 :
    pass
elif n//5 > 0 :
    for i in range(n//5) :
        stringA = stringA + 'V'

for j in range(n%5) :
    stringA = stringA + 'I'

print(stringA)
