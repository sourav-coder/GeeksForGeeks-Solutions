



#---coded by sourav sarkar---#




def mergeKArrays(a,n):
    '''
    :param a: given array
    :param n: size of row and column
    :return: merged sorted list
    '''
    b=[]
    for i in range(n):
        for j in range(n):
            b.append(a[i][j])
    return sorted(b)
    
