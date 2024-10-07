#find the square root of 54321 using approximation method

x=54321                        #saving the given number in a variable x
epsilon=0.1                      #we are setting a boundary range that this range tells that howmuch we are close to the answer
num_guess=0                      #we are initializing the number of guesses from zero
guess=0                          #initialized our guess from zero
increment=0.0001                 #howmuch we are incrementing the guess
while abs(guess**2-x)>=epsilon and guess**2<x:    #here looping to check conditions are like (1)how far is our square of guess is away from our x  and is it within the epsilon or crossed the epsilon (2)checking the important condition ie if the sqaure of the guess is less than x
    guess=guess+increment                      #making increments in the guess to reach the required sqaure value of x
    num_guess+=1                              #counting the number of guesses so that we can see how many guesses we had took to reach the result
print("num_guess=",num_guess)                 #the number of guesses are also being printed
if abs (guess**2-x)>=epsilon:                #exit the loop because our guess range is not at all eliigible to take
        print("Failed on the square root of x")
else:                                    #exit loop when guess**2 is close to the square root of x
        print(guess,"is close to the square root of x")
   
