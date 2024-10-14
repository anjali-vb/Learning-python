#find the square rot of 54321 using Newton-Raphson method whic is much efficient method

#According to Newton-Raphson method given a guess g for root of k a better guess is
        #  g = g-(g**2-k)/2g

k=54321
epsion=0.01
guess=k/2         #store the guess as half of the given number
num_guess=0
while (guess**2-k)>epsion:
 guess=guess-(((guess**2-k)/(2*guess)))
num_guess+=1
print(guess,"is close to the square root of k")
print(num_guess)
