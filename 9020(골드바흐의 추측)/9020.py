import sys

def sosu(i) :
    if i == 1 :
        return False
    for j in range(2,int(i**0.5)+1) :
        if i % j == 0 :
            return False
    else :
        return True

for i in range(int(sys.stdin.readline())) :
    n = int(sys.stdin.readline())
    
    A,B = n//2, n//2

    while 1 :
        if A < 2 :
            break
        if sosu(A) & sosu(B) :
            print(A,B)
            break
        else :
            A -= 1
            B += 1
