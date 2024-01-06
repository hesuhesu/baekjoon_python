stringA = input()
stringB = stringA.lower()

listA = list("abcdefghijklmnopqrstuvwxyz")
final_list = {}
for i in listA :
    if i in stringB :
        final_list[i] =  stringB.count(i)
    else :
        pass

tmp = [k for k,v in final_list.items() if max(final_list.values()) == v]

if len(tmp) > 1 :
    print("?")
else :
    print(tmp[0].upper())
