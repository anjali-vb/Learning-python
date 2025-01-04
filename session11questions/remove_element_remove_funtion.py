# L is a list .Use funtion to return the list but a particular element we required is removed


def remove_element(L,e):
    """
        L is a list which consists of elements called elem and also the belong to integer group
        returns a list with elements in L but the element equal to e are removed
    """
    for element in L:
     if element==e:
        L.remove(e)       #remove funtion is used to remove a oarticular element which is equal to e
    return L
L=[1,2,3,4]
print(remove_element(L,2))
