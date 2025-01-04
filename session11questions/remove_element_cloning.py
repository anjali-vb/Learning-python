# first make a copy of the list then clear the list then return a list with all elements in L but the elements equal to e are removed
       

def remove_element(L,e):
    """
        L is a list which consists of integers
        first make a copy of the list
        then clear the list
        returns a list with all elements equal to e are removed
    """
    Lnew=L[:]             #first make a copy of the original list
    L.clear()             #clear the original list
    for i in L:         
        if i==e:
            L.append(i)
    return Lnew
L=[2,3,4,5]
print(remove_element(L,4))
Lin=[1,6,6]
