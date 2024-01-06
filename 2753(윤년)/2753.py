a = int(input())

if ((a % 4 == 0)&((a % 100 != 0)|(a % 400 == 0))) : # or 과 and 를 잘 활용하길
    print(1)
else :
    print(0)
    
