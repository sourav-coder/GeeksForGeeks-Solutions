#code

#coded by ss

for _ in range(int(input())):
    
    n=int(input())
    a=list(map(int,input().split()))
    c=99999999999
    for i in range(len(a)-1):
        c=min(c,a[i+1]-a[i])
    
    # print(c)
    f=0
    for i in a:
        if a.count(i+c)==False:
            f=i+c
            break
    if n==2:print((a[0]+a[1])//2)
    else:
        print(f)
    


    

    
