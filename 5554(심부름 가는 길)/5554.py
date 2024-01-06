import sys

n1 = int(sys.stdin.readline())
n2 = int(sys.stdin.readline())
n3 = int(sys.stdin.readline())
n4 = int(sys.stdin.readline())
result = n1+n2+n3+n4

if result > 59 :
    print(result//60)
    print(result%60)
else :
    print(0)
    print(result)
