num = int(input())

for i in range(num) :
    a,b = map(str, input().split())
    a = int(a)
    for i in b :
        print((i * a), end="")
    print("")
