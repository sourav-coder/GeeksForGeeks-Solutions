

#coded by ss

t=int(input())
for i in range(t):
    n=int(input())
    s=list(map(str,input().split()))
    s=sorted(s)
    print(s[0],s[len(s)-1])
    #print(s)
