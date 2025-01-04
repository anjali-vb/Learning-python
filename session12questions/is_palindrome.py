#write a code to show true and reverse each letter of the list if the list x is a palindrome or false otherwise

def is_palindrome(x):
    """
        x is a list which consists of characters of a string
        returns true if list ,x is a palindrome or false otherwise
    """
    Lnew=x[:]
    print('before reverse',Lnew,x)
    Lnew.reverse()
    print('after reverse',Lnew,x)
    if Lnew==x:
        return true
    else:
        return false
    
print(is_palindrome('ab'))    
