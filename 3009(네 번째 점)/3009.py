import sys

x_list, y_list = [], []
x4, y4 = 0, 0
for _ in range(3):
    x, y = map(int, sys.stdin.readline().split())
    x_list.append(x)
    y_list.append(y)

for i in range(3):
    if x_list.count(x_list[i]) == 1:
        x4 = x_list[i]
    if y_list.count(y_list[i]) == 1:
        y4 = y_list[i]

print(x4, y4)