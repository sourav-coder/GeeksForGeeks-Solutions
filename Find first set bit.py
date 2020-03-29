

#coded by ss

for _ in range(int(input())):
    n=bin(int(input())).replace('0b','')
    #print(n)
    
    a=list(reversed(n))
    #print(a)
    c=0
    for i in range(len(a)):
        if a[i]=='1':
            c=i+1
            break
    print(c)
        
