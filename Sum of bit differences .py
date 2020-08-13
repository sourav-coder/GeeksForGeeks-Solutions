
for _ in range(int(input())):
    n=int(input())
    c=0
    a=list(map(int,input().split()))
    for i in range(n-1):
        for j in range(i+1,n):
            s=bin(a[i]^a[j]).count('1')
            print(s)
            c+=s
    print(2*c)


