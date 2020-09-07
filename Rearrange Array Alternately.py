# # python programs by sourav

for _ in range(int(input())):
    input()
    a=list(map(int,input().split()))

    b=a.copy()

    a.sort()
    b.sort(reverse=True)
    j,k=0,0
    for i in range(len(a)):
        if i%2==0:
            print(b[j],end=' ')
            j+=1
        else:
            print(a[k],end=' ')
            k+=1
    print()
