

#coded by ss

for _ in range(int(input())):
    n=int(input())
    a=[]
    l=list(bin(n).replace('0b',''))
    for  i in range(len(l)):
        if l[i]=='1':
            c=1
            for j in range(i+1,len(l)):
                if l[j]!='0':c+=1
                else:
                    i=j+1
                    break
            a.append(c)
    print(max(a))
