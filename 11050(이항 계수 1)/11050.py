import sys

def factorial(n) :
    if n > 1 :
        return factorial(n-1) * n
    else :
        return 1
N,K = map(int, sys.stdin.readline().split())

print(factorial(N)//(factorial(N-K)*factorial(K)))
