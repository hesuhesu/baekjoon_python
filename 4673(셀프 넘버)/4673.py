def check_number():
    All_set = set(range(1, 10001))
    find_set = set()
    
    for num in range(1, 10001):
        for i in str(num):
            num += int(i)
            
        find_set.add(num)
        
    return sorted(All_set - find_set)


check_numbers = check_number()
    
for i in check_numbers:
    print(i)
