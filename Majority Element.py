

#coded by sourav sarkar


#code

for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    d={}
    for i in a:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    #print(d)
    t=max(d.values())
    #print(t)
    if t>n//2:
        for key,value in d.items():
            if value==t:
                print(key)
                break
    else:print(-1)



