input_a = int(input())
listA = []

for i in range(input_a):
    input_b = input()
    s = list(input_b)
    sum = 0
    for i in s:
        if i == "(":
            sum += 1
        elif i == ")":
            sum -= 1
            if sum < 0 :
                listA.append("NO")
                break
            
    if sum > 0:
        listA.append("NO")
    elif sum == 0 :
        listA.append("YES")
    else :
        pass

for i in listA :
    print(i)
