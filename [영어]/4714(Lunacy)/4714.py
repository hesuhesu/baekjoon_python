import sys

while 1 :
    X = float(sys.stdin.readline())
    if (X == -1.0):
        break
    print("Objects weighing %.2f on Earth will weigh %.2f on the moon." % (X, X*0.167))
