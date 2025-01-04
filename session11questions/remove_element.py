#write a code to remove a particular element from a list
def remove_all(L,e):
    """
        L is a list with elements which are equal to integers  i,
        e is an particular element in the list
        returns L with all the elements equal to e are removed
    """
    L1=L[:]        #first take a copy of the list
    L.clear()       #then clear the original list
    for i in L1:
     if i!=e:
       L.append(i)
    return L   
L=[1,2,2,3,4,4,5,2]
print(remove_all(L,2))
L2=[8,8,8,8,81]
print(remove_all(L,8))
L3=[4,5,6,6,6,6,]
print(remove_all(L,5))
