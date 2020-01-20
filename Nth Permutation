#coded by Sourav Sarkar

#IN Python


def per(a,n):
    k=-1
    for i in range(n-1,0,-1):
        if a[i]>a[i-1]:
            k=i-1
            break
    #print(k)
    if k==-1:print(list(reversed(a)))
    else:
        m=k+1
        l=-1
        for i in range(k+1,n):
            if a[k]<a[i] and  a[m]>a[i]:
                m=i
        #print(m)

        t=a[k]
        a[k]=a[m]
        a[m]=t
        b=sorted(a[k+1:])
        b1=a[:k+1]
        for  i in b:
            b1.append(i)

        for i in b1:
            print(i,end=' ')
        print(' ')




t=int(input())
while(t>0):
    t-=1
    input()
    a=list(map(int,input().split()))
    per(a,len(a))




