# python programs by sourav


# code
for _ in range(int(input())):
    s = input().split('.')
    st=''
    for i in range(len(s)-1,-1,-1):
        # print(s[i],end='.')
        if i==0:
            st+=s[i]
        else:st+=s[i]+'.'
    print(st)





