import sys

N = int(sys.stdin.readline())
dicA = {}

for i in range(N) :
    name, state = map(str, sys.stdin.readline().strip().split())

    if state == "enter" :
        dicA[name] = state
    else :
        del dicA[name]

result = sorted(dicA.keys(), reverse=True)
for i in result :
    print(i)
