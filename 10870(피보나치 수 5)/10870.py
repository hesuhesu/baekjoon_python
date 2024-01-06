pabonachiList = [0,1,1]

for i in range(2,20) : # 18개가 더 추가되면 된다. n이 20이면 총 21개.
    pabonachiList.append(pabonachiList[i]+pabonachiList[i-1])

print(pabonachiList[int(input())])
