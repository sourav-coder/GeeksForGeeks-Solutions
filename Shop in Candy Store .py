t=int(input())
for test in range(t):
    a=[]
    c=0
    n,k=map(int,input().split())
    while(n>0):
        n-=1
        n-=k
        c+=1
    a=list(map(int,input().split()))
    a=sorted(a)
    print(sum(a[:c]),sum(a[:-(c+1):-1]))
