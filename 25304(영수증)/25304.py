final_price = int(input())
input_chance = int(input())
price = 0
for i in range(input_chance) :
    a,b = map(int, input().split())
    price += a*b

if price == final_price :
    print("Yes")

else :
    print("No")
