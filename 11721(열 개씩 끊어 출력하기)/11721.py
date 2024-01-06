import sys

stringA = sys.stdin.readline().strip()

for i in range(0, len(stringA), 10) :
    print(stringA[i:i+10])
