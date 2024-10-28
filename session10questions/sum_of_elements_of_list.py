#Add the elements of a list because lists also support iteration

def list_sum(L):
    """
        L is list consisting integers
        e,elements in the list
        returns the total sum of the elements of the list
    """
    total=0       #total is initiated
    for e in L:
        total+=e   #adding all the elements
    return total
print(list_sum([1,3,5]))
print(list_sum([3,3,5,3]))
print(list_sum([2,5,-1]))
        

