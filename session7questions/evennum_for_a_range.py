#print number between 1 and 10 and find whether they are odd or even

def is_even(i):
    """
    i,positive integer between 1 and 10
    prints numbers inbetween and also prints whether they are odd or even
    """
for i in range(1,11):
    if is_even(i):
        print(i,"even number")
    else:
        print(i,"odd number")
