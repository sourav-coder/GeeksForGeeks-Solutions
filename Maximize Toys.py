
#--using suffix array concept--
#coded by sourav sarkar

#code
for _ in range(int(input())):
    n,k=map(int,input().split())
    a=sorted(list(map(int,input().split())))
    c=s=0
    for i in a:
        s+=i
        if s>k:break
        c+=1
    print(c)
    
