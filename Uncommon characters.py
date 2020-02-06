




# coded by sourav sarkar


for _ in range(int(input())):
    s=list(input())
    s1=list(input())
    print(s,s1)
    a=[]
    for i in s:
        if i not in s1 and i not in a:
            a.append(i)
    for i in s1:
        if i not in a and i not in s:
            a.append(i)

    a=sorted(a)
    print(''.join(a))







