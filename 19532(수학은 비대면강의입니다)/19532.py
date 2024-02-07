import sys

a,b,c,d,e,f = map(int, sys.stdin.readline().split())

for i in range(-999, 1000):
    for j in range(-999, 1000):
        if (a*i) + (b*j) == c and (d*i) + (e*j) == f:
            print(i,j)

# 연립방정식
# print((c*e-b*f)//(a*e-b*d), (a*f-d*c)//(a*e-b*d))