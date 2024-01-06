import sys

available = list(map(int, sys.stdin.readline().split()))
requested = list(map(int, sys.stdin.readline().split()))
count = 0  
for i, j in zip(available, requested):
    if i-j < 0:
        count += (j-i)
print(count)
