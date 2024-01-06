listA = []
for i in range(9) :
    listA.append(list(map(int, input().split())))

int_x = 0
int_y = 0
result = -1
for i in range(9) :
    for j in range(9) :
        if listA[i][j] > result :
            result = listA[i][j]
            int_x = i + 1
            int_y = j + 1
        else :
            pass

print(result)
print(int_x,int_y)
