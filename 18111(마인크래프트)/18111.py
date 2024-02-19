import sys 
input = sys.stdin.readline

# 모든 땅의 높이를 h로 만드는데 걸리는 시간을 구하는 함수 
def get_time(h):
    add_num = 0   # 삽입할 블록의 개수 
    erase_num = 0 # 제거할 블록의 개수 

    # 0부터 256까지 각 높이의 경우를 모두 탐색
    for i in range(257):
        # 높이의 개수와 h와의 차를 구해줌 
        n, tmp = nums[i], i - h 
        # 개수가 0이라면 넘어감 
        if n == 0: continue 
        # 높이의 차가 음수일 경우 삽입할 블록의 개수 구해줌 
        if tmp < 0:
            add_num += (-tmp) * n 
        # 높이의 차가 양수일 경우 제거할 블록의 개수 구해줌 
        else:
            erase_num += tmp * n 
    
    # 만약 인벤토리에서 사용할 수 있는 블록이 있을 경우 
    if (erase_num + b) - add_num >= 0:
        # 시간을 구해줌 
        time = erase_num * 2 + add_num 
        return time 
    # 사용할 수 있는 블록이 없을 경우 
    else:
        return 1e9 + 1
            
n, m, b = map(int,input().split())

# 땅 높이 종류의 각 개수를 구해줌 
nums = [0] * 257 
for i in range(n):
    for j in list(map(int,input().split())):
        nums[j] += 1 

# 최소 시간과 그 때의 높이를 저장할 변수 
ans = 1e9 
height = 0

# 0부터 256까지 모든 땅을 각 높이로 만드는 시간을 구해줌 
for h in range(257):
    # 시간을 계산 
    time = get_time(h)
    # 최소값과 그 때의 땅 높이를 구해줌  
    if time <= ans:
        ans = time 
        height = h 

print(ans, height)