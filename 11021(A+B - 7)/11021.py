n = int(input())
a = []
for i in range(n) :
    n1,n2 = map(int,input().split())
    a.append(n1+n2)

for i in range(n) :
    print("Case #{}: {}".format(i+1,a[i]))
