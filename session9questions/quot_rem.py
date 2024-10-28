#Find the quotient and remainder using tuples
def quotient_and_remainder(x,y):
    """
        x and y are integers >0
        returns quotient and ramainder
    """
    
    quot=x//y
    rem=x%y
    return (quot,rem)
print(quotient_and_remainder(5,2))
