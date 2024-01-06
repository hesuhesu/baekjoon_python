import sys

N = int(sys.stdin.readline())

result = -1
for i in range(N) :
    A,B = map(int, sys.stdin.readline().split())

    if result == -1 and B-A >= 0 :
        result = B
    if result > B and B-A >= 0 :
        result = B

print(result)
