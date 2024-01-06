b = []

for i in range(9):
    b.append(int(input()))

c = b[0]
d = 1
for i in range(9) :

    if b[i] > c :
        c = b[i]
        d = i+1

print(c)
print(d)
