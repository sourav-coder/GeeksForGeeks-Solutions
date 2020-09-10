# # python programs by sourav



def helper(s):

    # print('pop -')

    if len(s)%2==0:

        n=s[:len(s)//2]
        # print(n)
        n+=n[::-1]
        # print(n)


    else:
        n=s[:len(s)//2+1]
        # print(n)
        n+=n[:len(n)//2+1][::-1]
        # print(n)



    return n








def solve(word):
    import math as m
    z=int(helper(word))

    if z>int(word):
        # print(1)
        return  z
    else:
        inc=1
        word=list(word)
        for i in range(m.ceil(len(word)/2)-1,-1,-1):
            word[i]=int(word[i])+inc
            inc=word[i]//10
            word[i]%=10

        return helper(word)



for _ in range(int(input())):
    n=int(input())
    if set(str(n))==1 and str(n)[0]=='9':
        print('1'+'0'*(len(str(n))-1)+'1')

    else:
        z=solve(str(n))
        # print(type(z))
        if type(z)!=int:
            d=int(''.join(map(str,z)))
        else:
            d=z
            # print(d)

        val=abs(d-n)
        # n-=1
        for _ in range(val):
            if str(n)==str(n)[::-1]:
                d=n
                break
            n-=1
        # real print --
        print(d)
















