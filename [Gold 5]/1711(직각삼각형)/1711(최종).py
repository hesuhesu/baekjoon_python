import sys

N = int(input())
points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            p1, p2, p3 = points[i], points[j], points[k]
            d1 = (p1[0]-p2[0])*(p1[0]-p2[0]) + (p1[1]-p2[1])*(p1[1]-p2[1])
            d2 = (p2[0]-p3[0])*(p2[0]-p3[0]) + (p2[1]-p3[1])*(p2[1]-p3[1])
            d3 = (p3[0]-p1[0])*(p3[0]-p1[0]) + (p3[1]-p1[1])*(p3[1]-p1[1])
            if 2 * max(d1,d2,d3) == d1+d2+d3:
                result += 1

print(result)
