import sys

N = int(sys.stdin.readline())
num1, num2 = map(int, sys.stdin.readline().split())
min_x, max_x = num1, num1
min_y, max_y = num2, num2
for _ in range(1,N):
    n1, n2 = map(int, sys.stdin.readline().split())
    if n1 > max_x :
        max_x = n1
    elif n1 < min_x :
        min_x = n1
    if n2 > max_y :
        max_y = n2
    elif n2 < min_y :
        min_y = n2
print((max_x - min_x) * (max_y - min_y))