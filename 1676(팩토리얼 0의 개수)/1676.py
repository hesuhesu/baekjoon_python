import sys

def factorial(n) :
    if n > 1 :
        return factorial(n-1) * n
    else :
        return 1

N = int(sys.stdin.readline())

result = 0
stringA = list(map(int, str(factorial(N))))
while 1 :
    if stringA[-1] == 0 :
        result += 1
        stringA.pop()
    else :
        break

print(result)
