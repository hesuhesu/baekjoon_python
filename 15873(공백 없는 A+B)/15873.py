import sys

stringA = sys.stdin.readline().strip()

if (len(stringA) == 2):
    print(int(stringA[0])+int(stringA[1]))
elif (len(stringA) == 3):
    if (stringA[1] == '0'):
        print(int(stringA[:2])+int(stringA[2:]))
    elif (stringA[2] == '0'):
        print(int(stringA[:1])+int(stringA[1:]))
else :
    print(20)
