#write  a version of the is_even funtion without return

def is_even(i):
    """
        i,which is a postitve integer
        returns has remainder If It is even,otherwise
    """
    print("without remainder")
    remainder=i%2
    has_rem=(remainder==0)
    print(has_rem)
    print("has reminder")
print(is_even(4))
