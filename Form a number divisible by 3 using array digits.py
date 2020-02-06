


# coded by sourav sarkar

#Form a number divisible by 3 using array digits



for _ in range(int(input())):
    input()
    a=list(map(int,input().split()))
    s=0
    for i in a:
        v=list(str(i))
        print(v)
        for i in v:
            s+=int(i)
        print(s)

    if s%3==0:print(1)
    else:print(0)

