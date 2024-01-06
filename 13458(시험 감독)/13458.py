import sys

num = int(sys.stdin.readline())

result = 0

studentList = list(map(int, sys.stdin.readline().split()))
main, sub = map(int, sys.stdin.readline().split())
for i in studentList :
    subsub = i - main
    result += 1
    if  subsub < 0 :
        pass
    elif subsub > 0 :
        if subsub % sub == 0 :
            result+= (subsub//sub)
        else :
            result += (subsub // sub) + 1  

print(result)
