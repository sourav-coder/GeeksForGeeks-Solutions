


# coded by sourav sarkar


for _ in range(int(input())):
    n=list(input())
    m=len(n)//2
    a=n[:m]
    b=n[m+1:]
    #print(a,b)
    s=su=0
    for i in a:s+=int(i)
    for i in b:su+=int(i)
    if s==su:print(1)
    else:print(0)
        






