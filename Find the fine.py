

#coded by sourav sarkar


for _ in range(int(input())):
    n,d=map(int,input().split())
    c=list(map(int,input().split()))
    p=list(map(int,input().split()))
    s=0
    if d%2==0:
        for i in range(len(c)):
            if c[i]&1==True:
                s+=p[i]
                print(s)
    else:
        s=0
        for i in range(len(c)):
            if c[i]%2==0:
                s+=p[i]
    print(s)



