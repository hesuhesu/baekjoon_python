import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

if ((A+B+C) == 180) :
    if (A == B == C) :
        print("Equilateral")
    elif ((A==B)|(B==C)|(A==C)) :
        print("Isosceles")
    else :
        print("Scalene")
else :
    print("Error")
