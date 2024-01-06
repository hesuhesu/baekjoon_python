import sys

while 1 :
    
    name, age, weight = map(str, sys.stdin.readline().strip().split())
    if name == '#' :
        break

    age = int(age)
    weigth = int(weight)
    if (age > 17) | (weigth >= 80):
        print(name, "Senior")
    else :
        print(name, "Junior")
