n = []

while 1 :
    a,b = list(map(int,input().split()))
    n.append(a+b)

    if (a == 0 & b == 0) :
        n.pop()
        break

for i in range(len(n)) :
    print(n[i])
