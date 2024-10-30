#square every element of list mutating the oriignal list

def square_list(L):
    """
        L, list consists of integers
        returns a list which consists of the square of the elements pf L in same order
    """
    for i in range(len(L)):    #means to square every element that comes under length of L
     L[i]=L[i]**2              #we can square the list Itself by using this formula because we have to square a list not the integer
    return L
L=[1,2,3,4]    
print(square_list(L))
print(square_list([3,5,7]))      #examples
print(square_list([8,9,10]))

