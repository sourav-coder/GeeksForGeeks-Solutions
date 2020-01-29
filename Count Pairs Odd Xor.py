


t=int(input())
while t>0:
    t-=1
    input()
    a=sorted(list(map(int,input().split())))
    c=d=0
    for i in a:
        if i%2==0:
            c+=1
        else:
            d+=1
    print(c*d)
