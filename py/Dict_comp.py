# a=range(1,10)
# d={i:i**2 if i%2==0 else i for i in a }
# print(d)
A=[1,2,3,6,4,5]
d={}
for i in range(len(A)):
    d[i]=A[i]
d1={v for i ,v in d.items() if v<v+1}
print(d)
print(d1)
