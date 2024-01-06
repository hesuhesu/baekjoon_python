import sys

word = list(map(str, sys.stdin.readline().rstrip("\n")))
listA = []

for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        first = word[:i] 
        second = word[i:j] 
        third = word[j:] 

        first.reverse()
        second.reverse()
        third.reverse()

        listA.append("".join(first + second + third))

print(min(listA))
