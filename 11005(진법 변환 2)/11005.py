import sys

N, B = map(int, sys.stdin.readline().split())
stringA = ''
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while N:
    stringA += str(arr[N%B])
    N //= B

print(stringA[::-1])