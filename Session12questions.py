#Make a list comprehension exmaple

def f(L):
    """
        L is a list with elements which are equal to e
        returns a new list with elements in L which are applied with a aprticular funtion
    """    
    Lnew=[]
    for e in L:
        Lnew.append(e**2)
        return Lnew
