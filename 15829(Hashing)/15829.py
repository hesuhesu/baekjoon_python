import sys

N = int(sys.stdin.readline())
stringA = sys.stdin.readline().strip()

result = 0
for i in range(N) :
    result += (ord(stringA[i])-96) * (31**(i))

print(result % 1234567891)
