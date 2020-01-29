

# Your task is to complete this function
# Function should return an integer

#--coded by sourav sarkar---#

def num(a, n, k):
    # Code here
    s=0
    for i in a:
        c=list(str(i))
        #print(c)
        s+=c.count(str(k))
    return s



