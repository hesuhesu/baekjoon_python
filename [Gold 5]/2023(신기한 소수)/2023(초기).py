num = int(input())

def present(n) :
    for k in range(2,n) :
        if n % k == 0 :
            return 0
    return 1

for i in range(2*10**(num-1)+1,10**(num)) :
    subList = 0
    for j in range(0,num):
        havenum = i // 10**j
        if present(havenum) == 0 :
            break
        elif present(havenum) == 1 :
            subList+=1
    if subList == num:
        print(i)
