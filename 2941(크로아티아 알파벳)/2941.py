stringA = input()

listA = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in listA :
    stringA = stringA.replace(i, '!')
print(len(stringA))
