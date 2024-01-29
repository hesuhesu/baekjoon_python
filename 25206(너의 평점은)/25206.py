import sys

subjectPoint = 0
Count = 0
dicA = {"A+" : 4.5, "A0" : 4.0, "B+" : 3.5, "B0" : 3.0,
        "C+" : 2.5, "C0" : 2.0, "D+" : 1.5, "D0" : 1.0,
        "F" : 0}
for i in range(20) :
    subjectName, credits, grade = list(map(str, sys.stdin.readline().split()))
    if (grade != 'P'):
        subjectPoint += dicA[grade] * float(credits)
        Count += float(credits)

print("%.6f" % (subjectPoint / Count))