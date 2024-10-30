#Square every element of list mutating original list and return list before funtion call and after funtion call

def square_list(L):
    """
        L is a list with integers
        returns a list elements before funtion call and after funtion call
    """
    for i in range(len(L)):
     L[i]=L[i]**2
    return L
L=[1,2,3,4,5,6]
print("before funtion call",L)
print('after funtion call',square_list(L))
                
