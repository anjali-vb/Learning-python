#write a funtion which returns a list in the same order but a particular element is removed

def remove_element(L,e):
    """
        L is a list
        e is a object of the list
        returns a list which is of same order but without any elements equal to e 
    """
    newlist=[ ]             #made an empty list
    for i in (L):
        if i!=e:            #condition is set to remove the unwanted element from the list
         newlist.append(i)
    return newlist
L=[1,2,3,4,5,6]
print("new list is",remove_element(L,6))
