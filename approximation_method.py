#find the square root of 54321 using approximation method

x=54321                          #saving the number in a variable x
epsilon=0.1                      #setting a boundary range to know how much close we are to answer
num_guess=0                      #initializing the number of guesses from zero
guess=0                          #initialized our guess from zero
increment=0.0001                 #howmuch we are incrementing the guess
while abs(guess**2-x)> epsilon and guess**2 <x:    #looping conditions are made(1)epsilon=howmuch close we are to answer ie guess**2-x,here first condition is if guess**2-x>epsilon we fixed then It exits loop(2)when sq of our guess is not meeting our x
    guess=guess+increment                      #making increments in the guess to reach the required sqaure value of x
    num_guess+=1                              #counting the number of guesses so that we can see how many guesses we had took to reach the result                 
if abs (guess**2-x)> epsilon:                #exit the loop because our guess range is not at all elligible to take
    print("Failed on the square root of x")
else:                                       #exit loop when guess**2 is close to the square root of x
    print(guess,"is close to the square root of x")
print("num_guess=",num_guess)               #her number of guesses is also being printed
   
