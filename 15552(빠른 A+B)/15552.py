import sys

n = int(input())

for i in range(n) :
    i,j = map(int, sys.stdin.readline().split()) # input() 대신 사용가능함.
    print(i+j)
