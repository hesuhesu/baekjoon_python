import sys

me = sys.stdin.readline().strip()
doc = sys.stdin.readline().strip()

if len(me) >= len(doc) :
    print("go")
else :
    print("no")
