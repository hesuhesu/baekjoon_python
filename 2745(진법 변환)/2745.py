import sys

listA = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N, B = map(str, sys.stdin.readline().split())
N = N[::-1]
B = int(B)
result = 0
for i, num in enumerate(N):
    result += (B ** i) * listA.index(num)
    
print(result)