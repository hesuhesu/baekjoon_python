import sys
 
def test(n1,n2) :
    return (n1+n2) * (n1-n2)

A,B = map(int, sys.stdin.readline().split())

print(test(A,B))
