import sys

T = int(sys.stdin.readline())
C_list = [25,10,5,1]
for _ in range(T):
    C = int(sys.stdin.readline())
    result = []
    for i in C_list:
        result.append(C // i)
        C %= i
    print(*result)