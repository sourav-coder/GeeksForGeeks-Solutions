

#coded by ss


for _ in range(int(input())):
    n=int(input())
    p=0
    a=list(map(int,input().split()))

    for i in a:
        p=p^i
    print(p)
