# find the square root of 0.5 by using bisection method

x=0.5         #for numbers less than one we have to change the endpoints a quite bit
epsilon=0.01   #epsilon= how far away we are from answer 
if x<=1:       #here the number x is less than 1 so if it is the low endpoint will be x and high will be 1
    low=x      
    high=1
else:          #here the number x is less than 1 so if it is the low endpoint will be x and high will be 1
    low=1
    high=x
guess=(low+high)/2         #midpoint is found
while abs(guess**2-x)>epsilon:       #looping condition is made ,abs is added to 
 if guess**2<x:
     low=guess
 else:
     high= guess
 guess=(low+high)/2
print (guess,"is close to the square root of x") 

    
