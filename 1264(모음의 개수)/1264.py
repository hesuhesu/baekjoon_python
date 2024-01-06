import sys

listA = ['a','e','i','o','u']

while 1 :
    stringA = sys.stdin.readline().strip()
    stringA = stringA.lower()
    if stringA == '#' :
        break
    else :
        stringA = list(stringA)
        result = 0
        for i in listA :
            result += stringA.count(i)
        print(result)
