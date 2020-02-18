

'''Given a sequence of strings, the task is to find out the second most repeated (or frequent) string in the given sequence.

Note: No two strings are the second most repeated, there will be always a single string.'''
#code

# coded by ss
t= int(input())
while (t > 0):
    t -= 1
    input()
    s=input().split(' ')
    #print(s)
    from collections import Counter
    z=Counter(s)
     #print(z.most_common())
    x=z.most_common()
    f=x[1]
    print(f[0])
