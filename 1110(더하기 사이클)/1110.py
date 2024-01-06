num = int(input())

if num < 10 :
    num = num * 10

numup = num // 10
numdown = num % 10
count = 0
while 1 :
    Aprice = numup + numdown
    Bprice = (numdown * 10) + (Aprice % 10)
    numup = numdown
    numdown = Aprice % 10

    count += 1
    if Bprice == num :
        break

print(count)
