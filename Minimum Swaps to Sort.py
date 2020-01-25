


#---coded by sourav sarkar----#


def minSwaps(a, n):
    # Code here
    c = 0

    for i in range(n-1):
        m=i
        for j in range(i,len(a)):
            if a[m]>a[j]:
                m=j
        if m!=i:
            a[m],a[i]=a[i],a[m]
            c+=1
    return c





t=int(input())
while t>0:
    t-=1
    input()
    a=list(map(int,input().split()))
    print(minSwaps(a,len(a)))
