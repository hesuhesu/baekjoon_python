import sys

stringA = sys.stdin.readline().strip()

stringA = stringA.replace("XXXX", "AAAA")
stringA = stringA.replace("XX", "BB")

if 'X' in stringA:
    print(-1)
    
else:
    print(stringA)
