


#coded by sourav sarkar

a=[3,10,21,36]
c=len(a)
while(1):
    c+=1
    if c==103:break
    d=(a[len(a)-1]-a[len(a)-2])+4+a[len(a)-1]
    a.append(d)

#print(a)]
for _ in range(int(input())):
    n=int(input())
    try:
        print(a[n-1])
    except:IndexError
