#Using funtions find a number which is even or not using memory bindings

def is_even(i):
    """
       i,positive integer
       returns True if it is postive number, otherwise false
    """
    if i%2==0:
        return True
    else:
        return False
a=is_even(3)
print(a)
b=is_even(4)
print(b)
c=is_even(9)
print(c)
