

#---coded by sourav sarkar---#

# ---this is somewhat a tricky problem just need to convert an integer into the base of 62 similar to int to binary conversions....

#code
a=list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
#print(a)


t=int(input())
while t>0:
    t-=1
    s=''
    n=int(input())
    n1=n
    while(n>0):
        r=n%62
        s+=a[r]
        n//=62
    print(''.join(list(reversed(s))))
    print(n1)


