


# coded by sourav sarkar



for _  in range(int(input())):
    n,m=map(int,input().split())
    a='{0:016b}'.format(n)
    b='{0:016b}'.format(m)
    #print(a,b)
    c=0
    for i in range(16):
        if a[i]!=b[i]:
            c+=1
            if c>1:break
    #print(c)
    if c==1:print(c)
    else:print(0)
