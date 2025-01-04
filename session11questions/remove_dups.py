#Remove dups from L1 which are in L2
def remove_dups(L1,L2):
    """
        L1 and L2 are two sets which consists of the integers i,
        returns L1 and L2 with all the elments common for bot of them are removed
    """
    L1_copy=L1[:]

    for i in L1_copy:
        if i in L2:
            L1.remove(i)  
    return L1
   
L1=[1,2,3,4]
L2=[1,2,5]
print(remove_dups(L1,L2))


    
