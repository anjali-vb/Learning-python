#Mutate the original list by appending the list with the elements equal to the length of the list by funtion

def append_elements(L):
    """
        L is a list consists of integers
        returns a list with original elements of list along with appended integers that comes under range of lengthof L
    """
    for i in range(len(L)):
        L.append(i)
    return L
L=[1,2,3,4]
print(append_elements(L))
L=[6,7,8,9]
print(append_elements(L))
L=[8,9,10,11]
print(append_elements(L))
