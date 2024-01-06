import sys

stringA = sys.stdin.readline().strip()
result = 0

while len(stringA) > 1 :
    stringA = str(sum(list(map(int, stringA))))
    result += 1

print(result)
if int(stringA) % 3 == 0 :
    print("YES")
else :
    print("NO")
