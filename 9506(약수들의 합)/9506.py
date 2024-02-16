import sys

while 1 :
    n = int(sys.stdin.readline())
    if n == -1 :
        break

    result = []
    for i in range(1,(n // 2) + 1):
        if n % i == 0 :
            result.append(i)
    
    if sum(result) == n :
        print(f"{n} = ", end = "")
        for i in range(len(result)) :
            if i == len(result) - 1 :
                print("{}".format(result[i]))
                continue
            print("{} + ".format(result[i]), end = "")
    else :
        print("{} is NOT perfect.".format(n))