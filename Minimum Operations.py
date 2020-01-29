


#this is a dp-problem but i have done without it

#---coded by sourav sarkar--#

t = int(input())
while (t > 0):
    t-=1
    n=int(input())
    res=0
    while n:
        if n&1==1:
            n-=1
        else:
            n//=2
        res+=1
    print(res)
