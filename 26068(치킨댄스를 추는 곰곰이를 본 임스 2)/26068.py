import sys

num = int(sys.stdin.readline())

result = 0
for i in range(num) :
    intnum = int(sys.stdin.readline().strip()[2:])
    if intnum <= 90 :
        result += 1

print(result)
