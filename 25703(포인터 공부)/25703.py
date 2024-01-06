import sys

n= int(sys.stdin.readline())
print('int a;')
print('int *ptr = &a;')
if n==2:
    print('int **ptr2 = &ptr;')
elif n>=3:
    print('int **ptr2 = &ptr;')
    for i in range(3,n+1):
        star = '*'*i
        print('int {}ptr{} = &ptr{};'.format(star,i,i-1))
