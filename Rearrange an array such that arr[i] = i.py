


#coded by sourav sarkar
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=[-1 for i in range(n)]
    for i in range(n):
        if i in a:
            b[i]=i
    for i in b:print(i,end=' ')
    print()
