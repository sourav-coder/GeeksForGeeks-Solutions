# python programs by sourav



for _ in range(int(input())):

    n=int(input())
    f=2

    for i in range(1,n):

        if i+bin(i)[2:].count('1')==n:
            f=0
            print(i)
            break
    if f==0:
        print(0)
    else:print(1)




