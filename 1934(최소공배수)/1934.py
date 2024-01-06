import sys

def gcd(x, y): 
  if y == 0:
    return x
  else:
    return gcd(y, x % y)

K = int(sys.stdin.readline())

for i in range(K):
    x, y = map(int, input().split(" "))
    print((x*y)//gcd(x,y))
