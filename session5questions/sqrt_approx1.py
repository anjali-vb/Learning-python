#find the square root of 36 using approximation method

x=36                                          #saving the number in a variable
epsilon=0.1                                   #selecting a boundary range to know how close we are to answer
num_guess=0                                   #initializing the number of guesses
guess=0                                       #initializing guess value
increment=0.0001                              #unit of incrementation of the guess according to our requirement
while abs (guess**2-x)>epsilon and guess**2<x:   #looping conditions are made (1)epsilon=how close we are to answer ie guess**2-x, here first condition is if guess**2-x> epsilonthat is we fixed then it exits loop(2)when sq of our guess is not enough for meeting our x
    guess=guess+increment                        #guess is incremented on the unit of increment
    num_guess+=1                                 #number of guesses is counted
if abs(guess**2-x)>epsilon:                  #if epsilon(guess**2-x)>espsion we fixed then further guesses are unreasonable
    print("failed on square root of x")
else:
    print(guess,"is close to the square root of x")     
print("number_guess= ",num_guess)    

