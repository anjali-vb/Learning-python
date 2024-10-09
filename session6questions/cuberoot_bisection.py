#find the cuberoot of 27 by using bisection method

cube=27                #saving the number in a variable                   
epsilon=0.01           #selecting a boundary range to know how close we are to answer       
low=0                  #here two endpoints are set for easy calculation            
high=cube              
guess=(low+high)/2     #midpoint is found
while abs(guess**3-cube)>epsilon:    #looping conditiion is made- epsilon ie guess**2-x>epsion we had set
 if guess**3<cube:           #if guess**3<cube, then guess will bw in low range
    low=guess
 else:                        #if guess**3<cube, then guess will bw in low range
    high=guess
 guess=(low+high)/2           #new midpoint is found
print(guess)
    
 
