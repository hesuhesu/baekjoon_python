import sys

X,Y = map(str, sys.stdin.readline().strip().split())

X1 = X[::-1]
Y1 = Y[::-1]
X1 = int(X1)
Y1 = int(Y1)
result = X1 + Y1
result = str(X1+Y1)[::-1] 

print(int(result))
