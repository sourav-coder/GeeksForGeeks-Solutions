#coded by ss


def fun(a):
    for i in range(len(a)-1,0,-1):
        if a.count(a[i])>=2:
            
            return a[i]
    return -1


from collections import Counter
for _ in range(int(input())):
    
    input()
    a=list(map(int,input().split()))
    c=fun(a)
    if c!=-1:print(a.index(c)+a.count(c)-1,c)
    else:print(-1)

