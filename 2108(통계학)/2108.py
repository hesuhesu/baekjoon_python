import sys
from collections import deque, Counter

dq = deque()
num = int(sys.stdin.readline())

for i in range(num) :
    dq.append(int(sys.stdin.readline()))

dq = sorted(dq)

count = Counter(dq).most_common() 
# [('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)] 처럼 개수가 많은거대로 정렬
print(round(sum(dq)/num))
print(dq[num//2])
if len(dq) > 1 :
    if count[0][1] == count[1][1] : # 최빈값의 value값. 두번째 값의 value값.
        print(count[1][0])
    else :
        print(count[0][0])
else :
    print(count[0][0])

print(max(dq) - min(dq))
