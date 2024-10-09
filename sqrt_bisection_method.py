#find the sqrt of 9 by using bisection search method

x=9                     #saving the number in a variable
epsilon=1               #selecting a boundary range to know how close we are to answer
num_guess=0             #number of guesses are initialized
low=0                   #here two endpoints are set for easy calculation
high=x                   
guess=(low+high)/2.0    #midpoint is founded
while abs (guess**2-x)>epsilon:     #looing conditiion is made- epsilon ie guess**2-x>epsilon range we had set
 if guess**2<x:                     #if guess**2<x, then guess will be low
    low=guess
 else:                              #if guess**2>x, then guess will be high
    high=guess
 guess=(low+high)/2.0               #new midpoint is found according to the new guess range status
num_guess+=1                        #number of guess is counted
print(guess," is close to the square root of x")           
print("num_guess=",num_guess)
