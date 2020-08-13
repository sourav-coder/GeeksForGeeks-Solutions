
def fun(a,b,c):
    if b==0:return 1

    elif b%2==0:
        return fun((a*a)%c,b//2,c)
    else:
        return (a*fun((a*a)%c,(b-1)//2,c))%c






for _ in range(int(input())):
    a,b,c=map(int,input().split())
    print(fun(a,b,c))
