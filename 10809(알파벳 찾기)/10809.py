stringA = list(input())
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in alphabet :
    if i in stringA :
        print(stringA.index(i), end = ' ')
    else :
        print(-1, end = ' ')
