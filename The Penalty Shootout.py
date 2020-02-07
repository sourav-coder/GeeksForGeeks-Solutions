

#coded by  sourav sarkar

for _ in range(int(input())):
    a=list(input())
    c=0
    for i in range(len(a)):
        if a[i]=='2' and a[i+1]=='1':
            i+=2
            c+=1
    print(c)
