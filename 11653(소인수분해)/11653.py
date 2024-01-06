import sys

num = int(sys.stdin.readline())

m = 2
while num !=1:  
  if num%m==0: 
    print(m) 
    num = num//m
  else:
    m += 1
