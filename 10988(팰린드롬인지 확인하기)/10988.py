import sys

word = list(str(sys.stdin.readline()))
word.pop()
if list(reversed(word)) == word:
    print(1)
else:
    print(0)