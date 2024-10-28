#Add the length of elements of a list

def sum_length(L):
    """
        L is the list
        returns the sum of the length of the eleemns of a list
    """
    total=0
    for s in (L):    #s is each element representation in list
     total+=len(s)
    return total
print (sum_length(["ab","abc","gf","ghi"]))
    
