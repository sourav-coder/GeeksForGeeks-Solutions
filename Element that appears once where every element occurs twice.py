#coded by ss
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    p=0
    for i in a:
        p=p^i
    print(p)
