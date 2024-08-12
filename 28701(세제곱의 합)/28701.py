import sys
N = int(sys.stdin.readline())
result_1 = 0
result_2 = 0
for i in range(1,N+1): result_1 += i
for i in range(1,N+1): result_2 += i ** 3
print(result_1)
print(result_1 ** 2)
print(result_2)
