num1 = int(input())
num2_str = list(input())
num2_int = list(map(int, num2_str))

sum = 0
for i in range(num1):
    sum += num2_int[i]

print(sum)
