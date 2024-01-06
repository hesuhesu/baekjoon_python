n = int(input())

final = []

for i in range(n) :
    
    num = list(map(int,input().split()))
    averge = sum(num[1:])/num[0]
    b = 0

    for hp in num[1:] :
        if hp > averge :
            b += 1
    
    final.append((b/num[0])*100)  ## %인 만큼 100을 곱해준다.
    
    
for i in range(n) :
    print("{0:.3f}%".format(final[i]))
