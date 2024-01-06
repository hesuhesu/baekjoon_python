import sys

n = int(sys.stdin.readline())

result = 1
for i in range(1,n+1) :
    result *= i
    
StringResult = str(result)
print(StringResult[-1])
