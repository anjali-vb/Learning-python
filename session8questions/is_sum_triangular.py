#Using funtions write a code which prints True whwn the continued sum of natural numbers is triangular

def is_triangular(n):
    """
        n, integer >0
        returns True if sum is triangular ie the continous sum of natural numbers is equal to natural number, 1+2+3+......+k
        otherwise, False   
    """
    total=0                #sum is initialized
    for i in range(n+1):   #n+1 is used to get the n also included 
     total+=i              #sum is counted
    if total==n:           #if the sum is equal to natural number 
        return True        #return is used instead of print to avoid the wired none from coming
    else:
        return False
print(is_triangular(1))
print(is_triangular(4))
print(is_triangular(-2))

    
    
