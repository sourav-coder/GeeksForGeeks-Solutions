

#coded by sourav sarkar

for _ in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    sum1=sum(a)
    sum2=sum(b)
    if (sum1-sum2)%2!=0:print(-1)
    else:
        d=(sum1-sum2)//2
        for i in b:
            if d+i in set(a):
                print(1)
                break
        else:
            print(-1)
