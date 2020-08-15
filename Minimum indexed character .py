
# code
import  re
for _ in range(int(input())):
    s = input()
    s=list(s)
    c=1
    patt = input()
    for i in s:
        if (re.search(i,patt)):
            print(i)
            c=0
            break
    if c==1:print('$')




