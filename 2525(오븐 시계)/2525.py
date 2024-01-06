a,b = map(int, input().split())
num = int(input())

b = num + b

if (b >= 60) :
    num1 = b // 60
    num2 = b % 60

    a += num1
    b = num2

if (a >= 24) :
    num1 = a % 24

    a = num1

print(a, b)
