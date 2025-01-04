#For getting more accurate answer in the bisection method use epsilon as an argument in the funtion
def bisection_method(x,epsilon):           #here epsilon is used as an argument to the funtion
    """
        x is an integer >0
        epsion is the range of the difference between the square of the guess and the x
        returns the square root of the x
    """
    low=0
    high=x
    guess=(low+high)/2
    while abs(guess**2-x)>epsilon:
        if guess**2<epsilon:
            low=guess
        else:
            high=guess
            guess=(low+high)/2
            return guess
print(bisection_method(123,0.001))       
print(bisection_method(144,0.001))       
print(bisection_method(36,0.001))       
print(bisection_method(49,0.001))       
