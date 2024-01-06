import sys

while 1 :
    stringA = sys.stdin.readline().strip()
    if stringA == 'END' :
        break
    print(stringA[::-1])
