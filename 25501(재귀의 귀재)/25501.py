num = int(input())

def recursion(s, l, r,number):
    listA = []
    if l >= r: 
        listA.append(1)
        listA.append(number)
        return "{} {}".format(listA[0], listA[1])
    elif s[l] != s[r]: 
        listA.append(0)
        listA.append(number)
        return "{} {}".format(listA[0], listA[1])
    else: 
        return recursion(s, l+1, r-1, number+1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 1)

count_num = 0

for i in range(num) :
    print(isPalindrome(input()))
