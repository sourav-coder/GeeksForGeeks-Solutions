



#---CODED BY SOURAV SARKAR----#



#Kadane's Algorithm


t = int(input())
while (t > 0):
    t -= 1
    input()
    a=list(map(int,input().split()))
    lsum=a[0]
    gsum=a[0]
    for i in range(1,len(a)):
        lsum=max(a[i],a[i]+lsum)
        gsum=max(gsum,lsum)

    print(gsum)
