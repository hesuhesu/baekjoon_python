import sys

num1,num2 = map(int, sys.stdin.readline().split())

def mini(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def large(a, b):
    return a * b // mini(a, b)

print(mini(num1, num2))
print(large(num1, num2))
