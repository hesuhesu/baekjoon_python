import sys

N = int(sys.stdin.readline())
bitMasking = list(bin(N)[2:])[::-1]

threeJin = 1
result = 0
for i in bitMasking :
    result += int(i) * threeJin
    threeJin *= 3

print(result)
