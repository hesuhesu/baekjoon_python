import sys

result = 0
while 1 :
    num = int(sys.stdin.readline())
    if num == -1 :
        break
    result += num

print(result)
