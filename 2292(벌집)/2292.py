import sys

n = int(sys.stdin.readline())

n_count = 1
result = 1
while 1 :
    if (n <= n_count) :
        break
    n_count += 6 * result
    result += 1 
print(result)
