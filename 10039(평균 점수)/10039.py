# 특정 조건을 붙인 평균값 문제

a = [] 
b = 0

for i in range(5) :
    a.append(int(input()))
    if a[i] < 40 :
        a[i] = 40

for i in range(5) :
    b += a[i]
c = int(b/5)
print(c)
