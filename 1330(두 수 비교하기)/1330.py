a, b = input('숫자 두 개를 입력하세요: ').split()
a = int(a)    
b = int(b)

if a > b : 
    print('>')
elif a == b :
    print('==')
else : 
    print('<')
