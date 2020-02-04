

#User function Template for python3


#coded by sourav sarkar

def printMinIndexChar(s,pat):
    s=list(s)
    pat=list(pat)
    l=120
    for i in pat:
        if i in s:
            l=min(l,s.index(i))
    
    if l==120:
        return '$'
    else:
        try:
            return ''.join(s[l])
        except:IndexError
    #return required char
