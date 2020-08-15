# python programs by sourav


# code
from itertools import permutations
for _ in range(int(input())):
    s=input()
    s=''.join(list(sorted(s)))
    # print(s)
    p=list(permutations(s))

    for i in p:
        for j in i:
            print(j,end='')
        print(' ',end='')
    # print(len(p))
    print()





