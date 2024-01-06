import sys

n = int(sys.stdin.readline())

RGB = []
for i in range(n) :
    RGB.append(list(map(int, sys.stdin.readline().split())))

for j in range(1,n) :
    RGB[j][0] = min(RGB[j-1][1], RGB[j-1][2]) + RGB[j][0]
    RGB[j][1] = min(RGB[j-1][0], RGB[j-1][2]) + RGB[j][1]
    RGB[j][2] = min(RGB[j-1][0], RGB[j-1][1]) + RGB[j][2]

print(min(RGB[n-1]))
