a=[1,1]
b=[1,1]
for i in range(2,20):
    x=a[i-1]+a[i-2]
    a.append(x)
    if x % 2 != 0:
        b.append(a[i])
#print(a)
#print(b)
set(b)
print(sum(b))
