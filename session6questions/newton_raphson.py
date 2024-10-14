#find the sqaure root of 24 using Newton-Raphson method
 
   #according to Newton-Raphson method for a given guess g for root of k a better guess is
            #  g= g-(g**2-k)/2*g

k=24
epsilon=0.01
guess=k/2
num_guess=0
while abs(guess**2-k)>epsilon:
 guess=guess-(((guess**2)-k)/(2*guess))
num_guess+=1 
print(num_guess)
print(guess,"is close to the sqaure root of k")
    
