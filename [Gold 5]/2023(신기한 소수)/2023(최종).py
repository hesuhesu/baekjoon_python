import sys
input = sys.stdin.readline

n = int(input())

def find(x):
    for i in range(2, int(x**0.5) + 1):
        if int(x) % i == 0:
            return False
    return True

def dfs(num):
    # n 자릿수 도달 시 멈춤
    if len(str(num)) == n:
        print(num)
    else:
        for i in range(10):
            temp = num * 10 + i
            # 10 곱하고 i 더해서 자릿수 늘린 수가 소수일때만
            if find(temp):
                dfs(temp)

dfs(2)
dfs(3)
dfs(5)
dfs(7)
