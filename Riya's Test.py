

#coded by ss

t=int(input())
while t>0:
    t-=1
    s=input()
    m=len(s)//2
    s1=s[:m]
    if len(s)%2!=0:s2=s[m+1:]
    else:s2=s[m:]
    #print(s1,s2)
    if sorted(s1)==sorted(s2):
        print('YES')
    else: print('NO')
