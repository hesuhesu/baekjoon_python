S = input()
if len(S) <= 2 or not (S[0] == '\"' and S[-1] == '\"'):  # 길이가 2이하 또는 정확한 문자열이 아닌 경우
    print("CE")
else:
    print(S[1:-1])