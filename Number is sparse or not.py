
#coded by ss

for _ in range(int(input())):
    n=int(input())
    f=1
    l=list(bin(n).replace('0b',''))
    print(l)
    for  i in range(0,len(l)):
        try:
            if l[i]=='1':
                if l[i+1]=='1':
                    f=0
                    break
        except:IndexError

    print(f)






