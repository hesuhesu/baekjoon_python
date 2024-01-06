import sys

count = 1
while 1 :
    
    listA = list(map(int, sys.stdin.readline().split()))
    if listA[0] == 0 :
        break
    
    print(f'Case {count}: Sorting... done!')
    count += 1
