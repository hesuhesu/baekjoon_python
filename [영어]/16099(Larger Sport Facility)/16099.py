import sys

for i in range(int(sys.stdin.readline())) :
    lt, wt, le, we = map(int, sys.stdin.readline().split())
    
    if (lt * wt) > (le * we) :
        print('TelecomParisTech')
    elif (lt * wt) < (le * we) :
        print('Eurecom')
    else :
        print('Tie')
