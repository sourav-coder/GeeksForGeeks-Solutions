

#coded by ss

t=int(input())
for i in range(t):
    s=input()
    s=list(s)
    c=[]
    for i in s:
        if c.count(i)==0:
            c.append(i)
    print(''.join(c))
            
    
