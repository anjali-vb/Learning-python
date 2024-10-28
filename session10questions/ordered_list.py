#Write a code which returns a list containing all ints inorder from 0 to n

def make_ordered_list(n):
    """
        n is a positive integer
        returns a list which contains all the elements from 0 to n (including n)
    """
    mylist=[ ]                 #initially make an empty list
    for i in range(0,n+1):     #for the range n+1 is given because we have to include n also
        mylist.append(i)
    return mylist
print("The ordered list is",make_ordered_list(6))
print(make_ordered_list(3))
print(make_ordered_list(10))
