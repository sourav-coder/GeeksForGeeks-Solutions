
#   funtion to display  the counts of anagrams in increasing order
#    coded by Sourav Sarkar
def fun(a,n):
    b=[]
    for i in a:

        i=sorted(i)
        i=''.join(i)
        b.append(i)
    #print(b)
    d={}
    for i in b:
        if i  in d:
            d[i]+=1
        else:
            d[i]=1
    #print(d)

    c=[]
    for i in d.values():c.append(i)
    c=sorted(c)
    for i in c:
        print(i,end=' ')
    print(' ')





t=int(input())
while (t>0):
    t-=1
    input()
    a=list(map(str,input().split()))
    fun(a,len(a))
    
