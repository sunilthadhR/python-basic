A="i'm sunil thadh"
b=[]
c=[]
# for i in range(len(A)):
#    b.append(ord(A[i]))
# print(b)
# for i in b:
#    if i not in c:
#       c.append(i)
# print(c)
for i in A:
    b.append(ord(i))
    for i in b:
        if i not in c:
            c.append(i)

print(c)


