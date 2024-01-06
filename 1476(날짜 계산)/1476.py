import sys

E, S, M = map(int, sys.stdin.readline().split())

Etest = 0
Stest = 0
Mtest = 0
year = 0

while 1 :
    year += 1
    Etest += 1 
    Stest += 1
    Mtest += 1

    if Etest > 15 :
        Etest = 1
    
    if Stest > 28 :
        Stest = 1
    
    if Mtest > 19 :
        Mtest = 1

    if (Etest == E) and (Stest == S) and (Mtest == M) :
        break

print(year)
