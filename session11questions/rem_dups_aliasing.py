#Remove dups from L1 which are in L2 using aliasing

def remove_dups(L1,L2):
    """
       L1 and L2 are two lists which consists of integers as elements which are i
       returns L1 with the duplicate elements which are common in L2 are removed
    """
    L1_copy=L1[:]
    for i in L1_copy:
        if i in L2:               #Aliasing means when you pass a list as a parameter to a funtion, you are making an alias.The actual parameter(from the funtion call is an alias for the formal parameter(from the funtion definition)
            L1.remove(i)
    return L1
La=[1,2,3,4,]
Lb=[1,2,4]
print(remove_dups(La,Lb))
