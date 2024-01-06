import sys

listA = []

for i in range(2):
    T,F,S,P,C = map(int, sys.stdin.readline().split())
    listA.append(T*6 + F*3 + S*2 + P + C*2)

for j in listA :
    print(j)
