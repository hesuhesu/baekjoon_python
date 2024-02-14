import sys

def round_fix(num): # 참고로 python round 함수로는 오답.
    # python 은 오사오입. 현 문제는 사사오입. 
    if(num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

n = int(sys.stdin.readline())
if n == 0 :
    print(0)
else :
    n_15 = round_fix(n * 0.15)
    result = []
    for _ in range(n):
        result.append(int(sys.stdin.readline()))
    result.sort()

    print(round_fix(sum(result[n_15:n-n_15]) / len(result[n_15:n-n_15])))