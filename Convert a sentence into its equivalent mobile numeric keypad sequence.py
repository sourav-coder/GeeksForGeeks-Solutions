


#coded by sourav sarkar



# for 3 letter keywords


def fun(i,s,n):
    str1 = ''
    n = str(n)
    if i == s[0]:
        str1 += n
    elif i == s[1]:
        str1 += n * 2
    elif i == s[2]:
        str1 += (n * 3)

    return str1


#  for 4 letter keywords


def  fun1(i,s,n):
    str1=''
    n=str(n)
    if i==s[0]:
        str1+=n
    elif i==s[1]:
        str1+=n*2
    elif i==s[2]:
        str1+=(n*3)
    elif i==s[3]:
        str1+=(n*4)
    return str1






# main function


t=int(input())
while t>0:
    t-=1
    s=input()
    c=''
    for i in s:
        if i in 'ABC':
            c+=fun(i,'ABC',2)
        elif i in 'DEF':
            c += fun(i, 'DEF', 3)
        elif i in 'GHI':
            c += fun(i, 'GHI', 4)
        elif i in 'JKL':
            c += fun(i, 'JKL', 5)
        elif i in 'MNO':
            c += fun(i, 'MNO', 6)
        elif i in 'PQRS':
            c += fun1(i, 'PQRS', 7)
        elif i in 'TUV':
            c+=fun(i,'TUV',8)
        elif i in 'WXYZ':
            c += fun1(i, 'WXYZ', 9)
        elif i==' ':
            c+='0'
    print(c)

