a = int(input())
b = list(map(int,input().split()))
c = b[0]
d = b[0]

for i in range(a) :
    if b[i] < c :
        c = b[i]
    elif b[i] > d :
        d = b[i]

print(c,d)
