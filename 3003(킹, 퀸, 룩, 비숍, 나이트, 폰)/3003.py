chess = [1,1,2,2,2,8]

a = list(map(int, input().split())) # list로 각각 정수값 받기.

for i in range(6) :  # 반복문을 이용한 해결.
    print(chess[i] - a[i], end = ' ')  # end = ' ' 를 통해 띄워쓰기.
